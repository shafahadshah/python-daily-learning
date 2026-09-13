name = "Shafahad"
age = 22

with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")