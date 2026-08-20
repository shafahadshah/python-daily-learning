commands: list[str] = [
    "start",
    "skip",
    "stop",
    "restart",
]

for command in commands:
    if command == "skip":
        continue

    if command == "stop":
        break

    if command == "restart":
        pass

    print(f"Processing: {command}")