def count_numbers(limit: int):
    for number in range(1, limit + 1):
        yield number


for number in count_numbers(5):
    print(number)