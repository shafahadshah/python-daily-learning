import json

user = {
    "name": "Shafahad",
    "age": 22,
    "role": "Backend Developer"
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)