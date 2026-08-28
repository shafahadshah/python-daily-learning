products: list[dict[str, object]] = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 699.99,
    },
]

for product in products:
    print(product["name"], product["price"])