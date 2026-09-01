def calculate_total(*numbers: int) -> int:
    total: int = 0

    for number in numbers:
        total += number

    return total


print(calculate_total(10, 20))
print(calculate_total(5, 10, 15, 20))