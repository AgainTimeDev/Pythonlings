#!/usr/bin/env python3
"""
Pythonlings - Learn Python through interactive exercises!
Inspired by rustlings.

Usage:
  python pythonlings.py watch    # Recommended: watch for changes
  python pythonlings.py list     # List all exercises
  python pythonlings.py run      # Run current exercise
  python pythonlings.py hint     # Show hint for current exercise
  python pythonlings.py verify   # Verify all exercises
"""

from __future__ import annotations

import argparse
import json
import os
import queue
import select
import subprocess
import sys
import termios
import threading
import time
import tty
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

VERSION = "0.1.0"
EXERCISES_FILE = Path(__file__).parent / "exercises.toml"
PROGRESS_FILE = Path(__file__).parent / ".pythonlings.json"
WATCH_POLL_INTERVAL = 0.5


# ─────────────────────────────────────────────────────────────────────────────
# TERMINAL COLORS
# ─────────────────────────────────────────────────────────────────────────────

class C:
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"


def _color_supported() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def col(text: str, *codes: str) -> str:
    if not _color_supported():
        return text
    return "".join(codes) + text + C.RESET


def hr(char: str = "─", width: int = 60) -> str:
    return col(char * width, C.DIM)


# ─────────────────────────────────────────────────────────────────────────────
# MINIMAL TOML PARSER (for exercises.toml only, no imports needed)
# ─────────────────────────────────────────────────────────────────────────────

def _parse_exercises_toml(path: Path) -> list[dict]:
    """
    Hand-rolled parser for the exercises.toml format.
    Supports [[exercise]] tables with simple strings and
    triple-quoted strings (for hints).
    """
    try:
        import tomllib  # Python 3.11+
        with open(path, "rb") as f:
            data = tomllib.load(f)
        return data.get("exercise", [])
    except ImportError:
        pass

    # Fallback: custom mini-parser
    text = path.read_text(encoding="utf-8")
    exercises: list[dict] = []
    current: dict | None = None

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line == "[[exercise]]":
            if current is not None:
                exercises.append(current)
            current = {}
            i += 1
            continue

        if current is None or not line or line.startswith("#"):
            i += 1
            continue

        if "=" in line:
            key, _, rest = line.partition("=")
            key = key.strip()
            rest = rest.strip()

            if rest.startswith('"""'):
                # Multi-line string
                rest = rest[3:]
                parts = []
                if '"""' in rest:
                    parts.append(rest[:rest.index('"""')])
                else:
                    parts.append(rest)
                    i += 1
                    while i < len(lines):
                        seg = lines[i]
                        if '"""' in seg:
                            parts.append(seg[:seg.index('"""')])
                            break
                        parts.append(seg)
                        i += 1
                current[key] = "\n".join(parts).strip()
            elif rest.startswith('"') and rest.endswith('"'):
                current[key] = rest[1:-1]
            elif rest.startswith("'") and rest.endswith("'"):
                current[key] = rest[1:-1]
            else:
                current[key] = rest

        i += 1

    if current is not None:
        exercises.append(current)

    return exercises


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE MODEL
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Exercise:
    name: str
    path: Path
    topic: str
    hint: str
    number: int  # 1-indexed


def load_exercises() -> list[Exercise]:
    if not EXERCISES_FILE.exists():
        print(col(f"Error: {EXERCISES_FILE} not found.", C.RED, C.BOLD))
        print("Run pythonlings from the project directory.")
        sys.exit(1)
    raw = _parse_exercises_toml(EXERCISES_FILE)
    exercises = []
    for i, entry in enumerate(raw, start=1):
        path = Path(__file__).parent / entry["path"]
        exercises.append(Exercise(
            name=entry["name"],
            path=path,
            topic=entry.get("topic", ""),
            hint=entry.get("hint", "No hint available."),
            number=i,
        ))
    return exercises


# ─────────────────────────────────────────────────────────────────────────────
# PROGRESS TRACKER
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Progress:
    current_index: int = 0
    completed: set[str] = field(default_factory=set)

    @classmethod
    def load(cls, exercises: list[Exercise]) -> Progress:
        p = cls()
        if PROGRESS_FILE.exists():
            try:
                data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
                p.current_index = data.get("current_index", 0)
                p.completed = set(data.get("completed", []))
            except (json.JSONDecodeError, KeyError):
                pass
        p._sync_current(exercises)
        return p

    def save(self) -> None:
        data = {
            "version": VERSION,
            "current_index": self.current_index,
            "completed": sorted(self.completed),
        }
        PROGRESS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def current_exercise(self, exercises: list[Exercise]) -> Exercise:
        idx = max(0, min(self.current_index, len(exercises) - 1))
        return exercises[idx]

    def mark_done(self, name: str) -> None:
        self.completed.add(name)

    def advance(self, exercises: list[Exercise]) -> bool:
        """Move to next not-yet-completed exercise. Returns True if moved."""
        for i in range(self.current_index + 1, len(exercises)):
            if exercises[i].name not in self.completed:
                self.current_index = i
                return True
        for i in range(len(exercises)):
            if exercises[i].name not in self.completed:
                self.current_index = i
                return True
        self.current_index = len(exercises) - 1
        return False

    def _sync_current(self, exercises: list[Exercise]) -> None:
        for i, ex in enumerate(exercises):
            if ex.name not in self.completed:
                self.current_index = i
                return
        self.current_index = len(exercises) - 1

    def stats(self, exercises: list[Exercise]) -> tuple[int, int]:
        return len(self.completed), len(exercises)


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE RUNNER
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class RunResult:
    exercise: Exercise
    success: bool = False
    stdout: str = ""
    stderr: str = ""
    runtime_ms: float = 0.0
    timed_out: bool = False

    def display_output(self) -> str:
        parts = []
        if self.stdout.strip():
            parts.append(self.stdout.rstrip())
        if self.stderr.strip():
            parts.append(self.stderr.rstrip())
        return "\n".join(parts)


def run_exercise(exercise: Exercise) -> RunResult:
    root = Path(__file__).parent
    t0 = time.monotonic()
    try:
        result = subprocess.run(
            [sys.executable, str(exercise.path)],
            capture_output=True,
            text=True,
            timeout=15,
            cwd=str(root),
        )
        elapsed = (time.monotonic() - t0) * 1000
        success = result.returncode == 0
        return RunResult(
            exercise=exercise,
            success=success,
            stdout=result.stdout,
            stderr=result.stderr,
            runtime_ms=elapsed,
        )
    except subprocess.TimeoutExpired:
        return RunResult(exercise=exercise, timed_out=True)


# ─────────────────────────────────────────────────────────────────────────────
# TERMINAL UI
# ─────────────────────────────────────────────────────────────────────────────

BANNER = """
  ╔══════════════════════════════════════════╗
  ║              Pythonlings                 ║
  ╚══════════════════════════════════════════╝
"""


def print_banner() -> None:
    print(col(BANNER, C.CYAN, C.BOLD))
    print(col(f"  Version {VERSION}  –  Learn Python through interactive exercises!\n", C.DIM))


def print_progress(done: int, total: int, width: int = 44) -> None:
    filled = int(width * done / max(total, 1))
    bar = col("█" * filled, C.GREEN) + col("░" * (width - filled), C.DIM)
    pct = f"{done}/{total}"
    print(f"  Progress: [{bar}] {col(pct, C.BOLD)}\n")


def clear_screen() -> None:
    os.system("clear" if os.name != "nt" else "cls")


def _indent(text: str, spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(pad + line for line in text.splitlines())


def print_watch_screen(
    exercises: list[Exercise],
    progress: Progress,
    result: RunResult,
    show_hint: bool = False,
) -> None:
    clear_screen()
    print_banner()

    done, total = progress.stats(exercises)
    print_progress(done, total)

    ex = result.exercise
    label = col(f"  Exercise {ex.number}/{total}: ", C.DIM) + col(ex.name, C.BOLD, C.WHITE)
    topic_label = col(f"  Topic: {ex.topic}", C.DIM)
    print(label)
    print(topic_label)
    print(f"  {col(str(ex.path.relative_to(Path(__file__).parent)), C.DIM)}")
    print()
    print(hr())
    print()

    if result.timed_out:
        print(col("  ⏱  TIMEOUT", C.RED, C.BOLD))
        print()
        print("  The exercise exceeded the time limit.")
        print("  Check for infinite loops.")
    elif result.success:
        print(col("  ✓  PASSED", C.GREEN, C.BOLD))
        if result.stdout.strip():
            print()
            print(col("  Output:", C.DIM))
            print(_indent(result.stdout.strip(), 4))
    else:
        print(col("  ✗  ERROR", C.RED, C.BOLD))
        out = result.display_output()
        if out:
            print()
            print(col("  Error output:", C.DIM))
            print(_indent(out, 4))

    print()

    if show_hint:
        print(hr())
        print()
        print(col("  💡 Hint:", C.YELLOW, C.BOLD))
        print(_indent(ex.hint.strip(), 4))
        print()

    print(hr())
    print()
    keys = [
        ("h", "Hint"),
        ("l", "List"),
        ("n", "Next"),
        ("p", "Back"),
        ("q", "Quit"),
    ]
    key_line = "   ".join(
        col(k, C.CYAN, C.BOLD) + col(f": {v}", C.DIM) for k, v in keys
    )
    print(f"  {key_line}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# FILE WATCHER (polling, no external dependencies)
# ─────────────────────────────────────────────────────────────────────────────

class FileWatcher(threading.Thread):
    def __init__(self, paths: list[Path], event_queue: "queue.Queue[Path]") -> None:
        super().__init__(daemon=True)
        self.paths = paths
        self.queue = event_queue
        self._stop_event = threading.Event()
        self._mtimes: dict[str, float] = {}

    def run(self) -> None:
        for p in self.paths:
            try:
                self._mtimes[str(p)] = p.stat().st_mtime
            except FileNotFoundError:
                self._mtimes[str(p)] = 0.0

        while not self._stop_event.is_set():
            time.sleep(WATCH_POLL_INTERVAL)
            for p in self.paths:
                key = str(p)
                try:
                    mtime = p.stat().st_mtime
                    if self._mtimes.get(key, 0.0) != mtime:
                        self._mtimes[key] = mtime
                        self.queue.put(p)
                except FileNotFoundError:
                    pass

    def stop(self) -> None:
        self._stop_event.set()


# ─────────────────────────────────────────────────────────────────────────────
# WATCH MODE
# ─────────────────────────────────────────────────────────────────────────────

@contextmanager
def _raw_mode():
    """
    Set the terminal to cbreak mode (single keypresses without Enter).
    Uses cbreak instead of raw so that \\n is still treated as \\r\\n,
    ensuring output renders correctly.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # cbreak: single characters, but no raw-mode side effects on output
        tty.setcbreak(fd)
        yield True
    except Exception:
        yield False
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except Exception:
            pass


def cmd_watch(exercises: list[Exercise], progress: Progress) -> int:
    file_queue: queue.Queue[Path] = queue.Queue()
    all_paths = [ex.path for ex in exercises]
    watcher = FileWatcher(all_paths, file_queue)
    watcher.start()

    show_hint = False
    needs_render = True

    try:
        with _raw_mode() as raw_mode:
            while True:
                if needs_render:
                    ex = progress.current_exercise(exercises)
                    result = run_exercise(ex)

                    if result.success:
                        progress.mark_done(ex.name)
                        progress.save()

                    print_watch_screen(exercises, progress, result, show_hint=show_hint)
                    needs_render = False

                # Keyboard input (non-blocking, 100ms timeout)
                if raw_mode:
                    r, _, _ = select.select([sys.stdin], [], [], 0.1)
                    if r:
                        ch = sys.stdin.read(1)
                        if ch in ("q", "\x03", "\x04"):
                            break
                        elif ch == "h":
                            show_hint = not show_hint
                            needs_render = True
                        elif ch == "n":
                            ex = progress.current_exercise(exercises)
                            if ex.name in progress.completed:
                                progress.advance(exercises)
                            elif progress.current_index < len(exercises) - 1:
                                progress.current_index += 1
                            show_hint = False
                            needs_render = True
                        elif ch == "p":
                            if progress.current_index > 0:
                                progress.current_index -= 1
                                show_hint = False
                                needs_render = True
                        elif ch == "l":
                            _show_list_overlay(exercises, progress)
                            needs_render = True
                else:
                    time.sleep(0.1)

                # Process file changes
                try:
                    while True:
                        changed_path = file_queue.get_nowait()
                        for ex in exercises:
                            if ex.path == changed_path:
                                if ex == progress.current_exercise(exercises):
                                    needs_render = True
                                elif ex.name in progress.completed:
                                    progress.mark_done(ex.name)
                                    progress.save()
                                    needs_render = True
                                break
                except queue.Empty:
                    pass

    finally:
        watcher.stop()
        clear_screen()
        done, total = progress.stats(exercises)
        if done == total:
            print(col("\n  🎉 All exercises completed! Congratulations!\n", C.GREEN, C.BOLD))
        else:
            print(col(f"\n  Goodbye! ({done}/{total} exercises completed)\n", C.CYAN))

    return 0


def _show_list_overlay(exercises: list[Exercise], progress: Progress) -> None:
    clear_screen()
    print_banner()
    done, total = progress.stats(exercises)
    print_progress(done, total)
    _print_exercise_table(exercises, progress)
    print()
    print(col("  Press any key to go back...", C.DIM))
    try:
        sys.stdin.read(1)
    except Exception:
        pass


# ─────────────────────────────────────────────────────────────────────────────
# COMMANDS
# ─────────────────────────────────────────────────────────────────────────────

def _resolve_exercise(exercises: list[Exercise], progress: Progress, name: str | None) -> Exercise:
    if name is None:
        return progress.current_exercise(exercises)
    for ex in exercises:
        if ex.name == name:
            return ex
    # Partial match
    matches = [ex for ex in exercises if name in ex.name]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print(col(f"Multiple exercises found for '{name}':", C.YELLOW))
        for m in matches:
            print(f"  {m.name}")
        sys.exit(1)
    print(col(f"Exercise '{name}' not found.", C.RED))
    print("Use 'python pythonlings.py list' to see all exercises.")
    sys.exit(1)


def cmd_run(exercises: list[Exercise], progress: Progress, name: str | None) -> int:
    ex = _resolve_exercise(exercises, progress, name)
    print()
    print(col(f"  Running '{ex.name}'...", C.DIM))
    print()

    result = run_exercise(ex)

    if result.timed_out:
        print(col("  ⏱  Timed out.", C.RED, C.BOLD))
    elif result.success:
        print(col("  ✓  Passed!", C.GREEN, C.BOLD))
        if result.stdout.strip():
            print()
            print(_indent(result.stdout.strip(), 4))
    else:
        print(col("  ✗  Error!", C.RED, C.BOLD))
        out = result.display_output()
        if out:
            print()
            print(_indent(out, 4))

    print()
    return 0 if result.success else 1


def cmd_hint(exercises: list[Exercise], progress: Progress, name: str | None) -> int:
    ex = _resolve_exercise(exercises, progress, name)
    print()
    print(col(f"  💡 Hint for {ex.name}:", C.YELLOW, C.BOLD))
    print()
    print(_indent(ex.hint.strip(), 4))
    print()
    return 0


def cmd_verify(exercises: list[Exercise], progress: Progress) -> int:
    print()
    print(col("  Verifying all exercises...", C.BOLD))
    print()

    all_passed = True
    for ex in exercises:
        result = run_exercise(ex)
        if result.timed_out:
            status = col("⏱ TIMEOUT  ", C.RED)
            all_passed = False
        elif result.success:
            status = col("✓ PASSED   ", C.GREEN)
        else:
            status = col("✗ ERROR    ", C.RED)
            all_passed = False

        name_col = col(f"{ex.name:<30}", C.WHITE)
        print(f"  {status}  {name_col}")

        if not result.success and not result.timed_out:
            out = result.display_output()
            if out:
                lines = out.strip().splitlines()[:5]
                for line in lines:
                    print(col(f"             {line}", C.DIM))
            print()

    print()
    if all_passed:
        print(col("  🎉 All exercises passed!", C.GREEN, C.BOLD))
    else:
        print(col("  Some exercises have errors.", C.RED))

    return 0 if all_passed else 1


def _print_exercise_table(exercises: list[Exercise], progress: Progress) -> None:
    current = progress.current_exercise(exercises)
    done_set = progress.completed

    current_topic = None
    for ex in exercises:
        if ex.topic != current_topic:
            current_topic = ex.topic
            print()
            print(col(f"  ── {ex.topic} ", C.BLUE, C.BOLD) + col("─" * max(0, 45 - len(ex.topic)), C.DIM))

        if ex.name in done_set:
            status = col("✓", C.GREEN)
        elif ex == current:
            status = col("▶", C.CYAN, C.BOLD)
        else:
            status = col("○", C.DIM)

        name = ex.name
        if ex == current:
            name = col(ex.name, C.CYAN, C.BOLD)
        elif ex.name in done_set:
            name = col(ex.name, C.DIM)

        path_str = col(str(ex.path.relative_to(Path(__file__).parent)), C.DIM)
        print(f"  {status}  {name:<28} {path_str}")


def cmd_list(exercises: list[Exercise], progress: Progress, topic: str | None = None) -> int:
    filtered = exercises
    if topic:
        filtered = [ex for ex in exercises if ex.topic == topic]
        if not filtered:
            topics = sorted(set(ex.topic for ex in exercises))
            print(col(f"\n  Unknown topic '{topic}'.", C.RED))
            print(f"  Available topics: {', '.join(topics)}")
            return 1

    print()
    print(col("  Pythonlings – Exercise Overview", C.BOLD, C.CYAN))
    done, total = progress.stats(exercises)
    filt_done = sum(1 for ex in filtered if ex.name in progress.completed)
    print(col(f"  {filt_done}/{len(filtered)} completed", C.DIM))

    _print_exercise_table(filtered, progress)
    print()
    return 0


def cmd_reset(exercises: list[Exercise], name: str) -> int:
    ex = _resolve_exercise(exercises, name=name, progress=Progress())
    print()
    print(col(f"  ⚠  Reset exercise '{ex.name}'?", C.YELLOW, C.BOLD))
    print(f"  File: {ex.path}")
    print()
    answer = input("  Really reset? [y/N]: ").strip().lower()
    if answer not in ("y", "yes"):
        print("  Cancelled.")
        return 0

    # Try git checkout
    result = subprocess.run(
        ["git", "checkout", "--", str(ex.path)],
        capture_output=True,
        cwd=str(Path(__file__).parent),
    )
    if result.returncode == 0:
        print(col(f"  ✓ '{ex.name}' has been reset.", C.GREEN))
    else:
        print(col("  Git checkout failed.", C.RED))
        print("  Please restore the file manually.")
        return 1
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# ENTRYPOINT
# ─────────────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="pythonlings",
        description="Learn Python through interactive exercises!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  watch           Recommended: watch for changes and run exercises
  run [NAME]      Run an exercise (default: current)
  verify          Verify all exercises
  hint [NAME]     Show hint for an exercise (default: current)
  list            List all exercises with status
  reset NAME      Reset an exercise to its original state

Examples:
  python pythonlings.py watch
  python pythonlings.py hint variables1
  python pythonlings.py run functions2
  python pythonlings.py list --topic functions
        """,
    )
    parser.add_argument("--version", action="version", version=f"pythonlings {VERSION}")

    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.required = False

    sub.add_parser("watch", help="Watch for changes (recommended)")

    p_run = sub.add_parser("run", help="Run an exercise")
    p_run.add_argument("exercise", nargs="?", metavar="NAME")

    sub.add_parser("verify", help="Verify all exercises")

    p_hint = sub.add_parser("hint", help="Show hint")
    p_hint.add_argument("exercise", nargs="?", metavar="NAME")

    p_list = sub.add_parser("list", help="List all exercises")
    p_list.add_argument("--topic", metavar="TOPIC", help="Filter by topic")

    p_reset = sub.add_parser("reset", help="Reset an exercise")
    p_reset.add_argument("exercise", metavar="NAME")

    args = parser.parse_args()

    if args.command is None:
        print_banner()
        parser.print_help()
        return 0

    exercises = load_exercises()
    progress = Progress.load(exercises)

    cmd = args.command
    if cmd == "watch":
        return cmd_watch(exercises, progress)
    elif cmd == "run":
        return cmd_run(exercises, progress, getattr(args, "exercise", None))
    elif cmd == "verify":
        return cmd_verify(exercises, progress)
    elif cmd == "hint":
        return cmd_hint(exercises, progress, getattr(args, "exercise", None))
    elif cmd == "list":
        return cmd_list(exercises, progress, getattr(args, "topic", None))
    elif cmd == "reset":
        return cmd_reset(exercises, args.exercise)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
