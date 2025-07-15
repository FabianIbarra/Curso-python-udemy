import os
os.system("cls" if os.name == "nt" else "clear")

import json

users = {
    "nombre": "Fabián",
    "edad": 30,
    "lenguajes": ["Python", "JavaScript", "C++"],
}

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

with open("users.json", "r") as file:
    data = json.load(file)
    print(data)