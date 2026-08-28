users: dict[str, dict[str, str]] = {
    "user1": {
        "name": "Alice",
        "role": "admin",
    },
    "user2": {
        "name": "Bob",
        "role": "user",
    },
}

print(users["user1"]["name"])
print(users["user2"]["role"])