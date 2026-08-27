# A dictionary containing other dictionaries
users: dict[str, dict[str, str | int]] = {
    "alice": {
        "full_name": "Alice Johnson",
        "age": 30,
        "email": "alice@example.com",
    },
    "bob": {
        "full_name": "Bob Smith",
        "age": 25,
        "email": "bob@example.com",
    },
}

# Access a nested value
print("Alice's email:", users["alice"]["email"])

# Modify a nested value
users["bob"]["age"] = 26
print("Bob's updated age:", users["bob"]["age"])

# Add a new nested key to a user
users["alice"]["phone"] = "+1-555-1234"
print("Alice's phone:", users["alice"]["phone"])

# Iterate over all users and their info
for username, info in users.items():
    print(f"Username: {username}")
    for key, value in info.items():
        print(f"  {key}: {value}")