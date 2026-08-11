from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


print(OrderStatus.PENDING.value)
print(OrderStatus.SHIPPED.value)
print(OrderStatus.DELIVERED.value)