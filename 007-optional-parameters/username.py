from typing import Optional


def get_username(username: Optional[str] = None) -> str:
    if username is None:
        return "Guest"

    return username


print(get_username())
print(get_username("Alice"))