def get_name_info(names: list[str]) -> tuple[int, str]:
    count = len(names)
    first_name = names[0]

    return count, first_name


users: list[str] = [
    "Alice",
    "Bob",
    "Charlie",
]

result = get_name_info(users)

print(result)