price: float = 99.99
quantity: int = 3
discount: float = 10.0

total: float = price * quantity
final_price: float = total - discount

print("Total:", total)
print("Final price:", final_price)
print("Discount applied:", final_price < total)