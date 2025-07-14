import os
os.system("cls" if os.name == "nt" else "clear")

# Nested Dictionaries: Diccionarios dentro de diccionarios, útiles para representar estructuras complejas
nested_dict = {
    "user1": {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "JavaScript"]
    },
    "user2": {
        "name": "Bob",
        "age": 25,
        "skills": ["Java", "C++"]
    },
    "user3": {
        "name": "Charlie",
        "age": 35,
        "skills": ["Go", "Rust"]
    }
}

for user, details in nested_dict.items():
    print(f"User: {user}")
    for key, value in details.items():
        if isinstance(value, list): # isinstance: revisa si value es una lista
            print(f"  {key}: {', '.join(value)}")
        else:
            print(f"  {key}: {value}")
    print()