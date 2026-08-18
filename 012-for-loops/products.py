products: list[str] = [
    "Laptop",
    "Phone",
    "Headphones",
]

for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")