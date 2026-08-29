products: list[str] = [
    "Laptop",
    "Phone",
    "Headphones",
]

prices: dict[str, int] = {
    product: 100
    for product in products
}

print(prices)