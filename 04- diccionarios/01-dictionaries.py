import os
os.system("cls" if os.name == "nt" else "clear")

# Diccionarios = Objetos(JSON)
# No están ordenados

dictionary = {
    "a": [1, 2 , 3],
    "b": True,
    "c": (4, 5, 6)
}

print(dictionary["a"][1])
print(dictionary["c"][-1])

user = {
    "name": "Fabián",
    "country": "México",
    "age": 24
}

print(user["name"])
print(user["country"])
print(user["age"])