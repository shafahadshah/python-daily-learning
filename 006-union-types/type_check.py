def process(value: int | str) -> str:
    if isinstance(value, int):
        return f"Number: {value}"

    return f"Text: {value}"


print(process(100))
print(process("hello"))