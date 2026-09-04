message: str = "Global"


def outer() -> None:
    message: str = "Outer"

    def inner() -> None:
        nonlocal message
        message = "Changed by inner"

    inner()
    print(message)


def show_local() -> None:
    message: str = "Local"
    print(message)


show_local()
outer()
print(message)