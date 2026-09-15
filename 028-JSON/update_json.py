import json

with open("user.json", "r") as file:
    user = json.load(file)

user["age"] = 23
user["role"] = "Python Backend Developer"

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

print(user)