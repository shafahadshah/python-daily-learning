with open("users.txt", "w") as file:
    file.write("Ali\n")
    file.write("Ahmed\n")

with open("users.txt", "r") as file:
    users = file.readlines()

for user in users:
    print(user.strip())