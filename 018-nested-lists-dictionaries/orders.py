orders: list[dict[str, object]] = [
    {
        "id": 101,
        "customer": "Alice",
        "items": ["Laptop", "Mouse"],
    },
    {
        "id": 102,
        "customer": "Bob",
        "items": ["Phone", "Headphones"],
    },
]

for order in orders:
    print(f"Order #{order['id']}")
    print(f"Customer: {order['customer']}")

    items = order["items"]

    if isinstance(items, list):
        for item in items:
            print(f"- {item}")                