def product_names(products: list[dict[str, str]]):
    for product in products:
        yield product["name"]


products = [
    {"name": "Laptop"},
    {"name": "Keyboard"},
    {"name": "Mouse"},
]

for name in product_names(products):
    print(name)