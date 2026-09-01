def show_user(**details: str) -> None:
    for key, value in details.items():
        print(f"{key}: {value}")


show_user(
    name="Alice",
    role="admin",
    city="Peshawar",
)