from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


print(OrderStatus.PENDING)
print(OrderStatus.SHIPPED)
print(OrderStatus.DELIVERED)