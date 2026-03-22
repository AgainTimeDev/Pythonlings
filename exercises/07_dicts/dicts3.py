# Topic: Dictionaries
# Exercise: dicts3

"""
Nested Dicts and Merging

Dicts can be nested:
    config = {
        "database": {
            "host": "localhost",
            "port": 5432
        }
    }
    config["database"]["host"]  → "localhost"

From Python 3.9 you can merge dicts:
    merged = {**base, **overrides}  # overrides wins
    merged = base | overrides       # Python 3.9+

Your tasks:
1. Access `config["server"]["timeout"]`
2. Implement `configure(base, override)`:
   - Returns a new dict
   - All entries from `base` are present
   - `override` wins on conflicts
"""


# ----- YOUR SOLUTION -----

config = {
    "server": {
        "host": "example.com",
        "port": 443,
        "timeout": 30,
    },
    "database": {
        "name": "production",
        "pool_size": 10,
    }
}

# TODO: Access the timeout value
timeout = None

# TODO: Access the database name
db_name = None


def configure(base, override):
    # TODO: Return {**base, **override}
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert timeout == 30, f"timeout should be 30, but got {timeout}"
    assert db_name == "production", f"db_name → {db_name!r}"

    base_config = {"debug": False, "timeout": 30, "retries": 3}
    extra = {"timeout": 60, "new": "value"}
    result = configure(base_config, extra)
    assert result["debug"] is False
    assert result["timeout"] == 60, "overrides should win"
    assert result["new"] == "value"
    assert result["retries"] == 3
    print("✓ dicts3 done!")
