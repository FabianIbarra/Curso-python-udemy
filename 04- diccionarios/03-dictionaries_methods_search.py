import os
os.system("cls" if os.name == "nt" else "clear")

user = {
    "name": "Fabián",
    "country": "México",
    "email": "fabi_iba4@hotmail.com",
    "age": 24,
    "numbers": [1, 2, 3, 4, 5]
}

# .get()
print(user.get("name"))
print(user.get("age"))

# in

print("name" in user.keys())
print("Fabián" in user.values())

# items

print(user.items())