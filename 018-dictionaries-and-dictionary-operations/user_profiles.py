user: dict[str, str | int] = {
    "name": "Alice",
    "age": 30,
    "role": "admin",
}

user["email"] = "alice@example.com"  # add a new key-value pair
user["age"] = 31                     # update an existing value
del user["role"]                     # delete a key-value pair

print(user)