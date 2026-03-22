# Pythonlings 🐍

> Learn Python through interactive exercises – inspired by [rustlings](https://github.com/rust-lang/rustlings).

Pythonlings guides you through small, focused exercises where you write and run real Python code. Each exercise has skeleton code with `None` placeholders – replace them with your solution!

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/AgainTimeDev/Pythonlings.git
cd Pythonlings

# 2. Start watch mode (recommended!)
python3 pythonlings.py watch
```

Python 3.8+ required. No external dependencies.

---

## How It Works

1. **Open** the displayed exercise file in your editor
2. **Solve** the task (replace `None` and `pass` with real code)
3. **Save** the file – watch mode detects changes automatically
4. **Press `n`** to move to the next exercise once it passes

When all tests pass, Pythonlings shows a success message and waits for you to press `n`!

---

## Commands

| Command | Description |
|---------|-------------|
| `python pythonlings.py watch` | **Recommended**: Watch for changes and run exercises |
| `python pythonlings.py list` | List all exercises with status |
| `python pythonlings.py run [NAME]` | Run a specific exercise |
| `python pythonlings.py hint [NAME]` | Show hint for an exercise |
| `python pythonlings.py verify` | Verify all exercises |
| `python pythonlings.py reset NAME` | Reset an exercise |

### Watch Mode Keybindings

| Key | Action |
|-----|--------|
| `h` | Toggle hint |
| `l` | Show exercise list |
| `n` | Next exercise (skip) |
| `p` | Previous exercise |
| `q` | Quit |

---

## Exercises

| # | Topic | Exercises | Content |
|---|-------|-----------|---------|
| 1 | **Introduction** | intro1–3 | Output, comments, type conversion |
| 2 | **Variables** | variables1–4 | Assignment, types, operators |
| 3 | **Functions** | functions1–5 | def, return, *args, **kwargs, scope |
| 4 | **Conditions** | if_else1–4 | if/elif/else, logic, ternary |
| 5 | **Loops** | loops1–5 | for, while, break, continue, enumerate, zip |
| 6 | **Strings** | strings1–4 | Methods, f-strings, slicing |
| 7 | **Lists** | lists1–4 | Methods, slicing, sorting |
| 8 | **Dictionaries** | dicts1–3 | Methods, inverting, nesting |
| 9 | **Tuples** | tuples1–2 | Immutability, unpacking |
| 10 | **Error Handling** | error_handling1–3 | try/except, finally, custom exceptions |
| 11 | **Classes** | classes1–4 | __init__, inheritance, magic methods |
| 12 | **Comprehensions** | comprehensions1–3 | List, dict, set, filter |
| 13 | **Iterators** | iterators1–2 | iter/next, __iter__/__next__ |
| 14 | **Generators** | generators1–2 | yield, generator expressions, send() |
| 15 | **Modules** | modules1–2 | import, __name__ == "__main__" |

**50 exercises total.**

---

## Example Exercise

```python
# Topic: Functions
# Exercise: functions1

"""
Defining functions

Use def to define a function...
"""

# ----- YOUR SOLUTION -----

def greet(name):
    # TODO: Return "Hello, {name}!"
    pass

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert greet("World") == "Hello, World!"
    print("✓ functions1 done!")
```

---

## Tips

- Always start with `python pythonlings.py watch` – it shows you exactly what to do
- Use `h` in watch mode for hints when you're stuck
- Read the error messages carefully – Python usually tells you exactly what's wrong
- You can skip exercises with `n` and come back later

Good luck! 🚀
