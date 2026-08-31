def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


total: float = calculate_total(25.5, 4)

print("Total:", total)