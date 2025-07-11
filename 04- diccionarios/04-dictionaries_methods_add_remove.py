import os
os.system("cls" if os.name == "nt" else "clear")

user = {
    "name": "Fabián",
    "country": "México",
    "email": "fabi_iba4@hotmail.com",
    "age": 24,
    "numbers": [1, 2, 3, 4, 5]
}

# .copy()
print(user)
new_user = user.copy()
new_user["age"] = 20
print(new_user)

# .pop()
print(user.pop("age"))
print(user)

# .popitem()
print(user.popitem())
print(user)

# .update()
user.update({"age": 24})
print(user)

# .append()
user["numbers"] = [1, 2, 3, 4, 5, 6]
user["numbers"].append(7)
print(user)

# .extend()
user["numbers"].extend([7, 8, 9])
print(user)

# .clear()
user.clear()
print(user)
print(new_user)

# del
del new_user["numbers"]
print(new_user)