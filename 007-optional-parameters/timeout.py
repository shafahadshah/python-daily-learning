def connect(timeout: int = 10) -> str:
    return f"Connecting with {timeout} seconds timeout"


print(connect())
print(connect(30))