numbers: tuple[int, ...] = (
    10,
    20,
    30,
    20,
)

print(len(numbers))
print(numbers.count(20))
print(numbers.index(30))
print(20 in numbers)