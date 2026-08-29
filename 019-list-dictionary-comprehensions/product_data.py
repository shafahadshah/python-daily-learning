
products: dict[str, float] = {
    "Laptop": 1000.0,
    "Phone": 700.0,
    "Headphones": 150.0,
}

discounted_prices: dict[str, float] = {
    name: price * 0.9
    for name, price in products.items()
}

print(discounted_prices)