products: list[str] = [
    "Laptop",
    "Phone",
]

products.append("Headphones")
products.insert(1, "Tablet")

products.remove("Phone")

print(products)