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


status: OrderStatus = OrderStatus.SHIPPED

message: str = get_status_message(status)

print(message)