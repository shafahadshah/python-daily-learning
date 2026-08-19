name: str = ""

while name != "quit":
    name = input("Enter your name: ")

    if name != "quit":
        print(f"Hello, {name}")