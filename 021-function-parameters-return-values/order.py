def calculate_order(
    price: float,
    quantity: int,
    discount: float,
) -> float:
    subtotal: float = price * quantity
    total: float = subtotal - discount

    return total


order_total: float = calculate_order(
    100.0,
    3,
    20.0,
)

print("Order total:", order_total)