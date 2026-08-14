from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float


product = Product(
    id=1,
    name="Laptop",
    price=999.99,
)

print(product)