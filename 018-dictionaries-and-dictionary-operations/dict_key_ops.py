dict_a: dict[str, int] = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
}

dict_b: dict[str, int] = {
    "banana": 2,
    "date": 4,
    "apple": 1,
}

# Dictionary keys behave like sets!
common_keys = dict_a.keys() & dict_b.keys()
all_keys = dict_a.keys() | dict_b.keys()
only_a = dict_a.keys() - dict_b.keys()

print("Common keys:", common_keys)
print("All keys:", all_keys)
print("Only in A:", only_a)

# Iterating over key-value pairs
print("--- Items in A ---")
for key, value in dict_a.items():
    print(f"{key}: {value}")