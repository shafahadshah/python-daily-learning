from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float


products = [
    Product(1, "Laptop", 999.99),
    Product(2, "Phone", 699.99),
    Product(3, "Headphones", 149.99),
]

for product in products:
    print(product)