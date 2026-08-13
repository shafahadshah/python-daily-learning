from typing import Optional


def connect(timeout: int = 10) -> str:
    return f"Connecting with {timeout} seconds timeout"


def get_username(username: Optional[str] = None) -> str:
    if username is None:
        return "Guest"

    return f"Welcome, {username}"


print(connect(30))
print(get_username("Alice"))