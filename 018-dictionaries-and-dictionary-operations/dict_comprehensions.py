# Create a dictionary from a list using a comprehension
squares: dict[int, int] = {n: n**2 for n in range(1, 6)}
print("Squares:", squares)

# Convert two lists into a dictionary (zip + comprehension)
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
people: dict[str, int] = {name: age for name, age in zip(names, ages)}
print("People:", people)

# Safe access with .get() – returns a default if key is missing
print("Age of Alice:", people.get("Alice"))
print("Age of Dave (missing):", people.get("Dave", "Not found"))