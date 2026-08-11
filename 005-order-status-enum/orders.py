from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


def get_status_message(status: OrderStatus) -> str:
    if status == OrderStatus.PENDING:
        return "Your order is being prepared."

    if status == OrderStatus.SHIPPED:
        return "Your order has been shipped."

    if status == OrderStatus.DELIVERED:
        return "Your order has been delivered."

    return "Unknown order status."


orders: list[OrderStatus] = [
    OrderStatus.PENDING,
    OrderStatus.SHIPPED,
    OrderStatus.DELIVERED,
]

for status in orders:
    print(get_status_message(status))