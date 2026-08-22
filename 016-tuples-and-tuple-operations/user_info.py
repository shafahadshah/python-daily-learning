def get_user() -> tuple[int, str]:
    user_id: int = 101
    username: str = "Alice"

    return user_id, username


user_id, username = get_user()

print("ID:", user_id)
print("Username:", username)