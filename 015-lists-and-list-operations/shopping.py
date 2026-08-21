prices: list[float] = [
    100.0,
    250.0,
    50.0,
]

total: float = sum(prices)

print("Number of items:", len(prices))
print("Total:", total)
print("Highest price:", max(prices))
print("Lowest price:", min(prices))