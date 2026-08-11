from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


def get_status_message(status: OrderStatus) -> str:
    return status.value


print(get_status_message(OrderStatus.PENDING))