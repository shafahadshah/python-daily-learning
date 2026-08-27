defaults: dict[str, str] = {
    "theme": "dark",
    "language": "en",
}

user_prefs: dict[str, str] = {
    "language": "fr",
    "font_size": "14",
}

# Method 1: update() mutates the original dictionary
defaults.update(user_prefs)
print("Updated defaults:", defaults)

# Method 2: | operator merges into a new dictionary (Python 3.9+)
base = {"theme": "dark", "layout": "grid"}
overrides = {"theme": "light", "spacing": "tight"}
merged = base | overrides
print("Merged new dict:", merged)