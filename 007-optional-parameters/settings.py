from typing import Optional


def connect(timeout: int = 10) -> str:
    return f"Timeout: {timeout} seconds"


def get_username(username: Optional[str] = None) -> str:
    if username is None:
        return "Guest"

    return username


print(connect())
print(get_username())
print(get_username("Alice"))