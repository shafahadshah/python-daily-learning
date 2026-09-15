import json

with open("user.json", "r") as file:
    user = json.load(file)

print(user["name"])
print(user["role"])