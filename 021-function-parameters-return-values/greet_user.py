def greet_user(name: str) -> str:
    return f"Hello, {name}!"


message: str = greet_user("Alice")

print(message)