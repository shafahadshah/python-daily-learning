def process(value: int | str) -> str:
    if isinstance(value, int):
        return f"ID: {value}"

    return f"Name: {value}"


print(process(101))
print(process("Alice"))