numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers: list[int] = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)