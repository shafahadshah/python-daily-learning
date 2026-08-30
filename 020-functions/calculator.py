def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


total: float = calculate_total(99.99, 3)

print("Total:", total)