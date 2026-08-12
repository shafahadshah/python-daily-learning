def process(value: int | str) -> str:
    if isinstance(value, int):
        return f"ID: {value}"

    return f"Name: {value}"


result1: str = process(101)
result2: str = process("Alice")

print(result1)
print(result2)