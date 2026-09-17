def square_numbers(numbers: list[int]):
    for number in numbers:
        yield number * number


values = [1, 2, 3, 4]

for square in square_numbers(values):
    print(square)