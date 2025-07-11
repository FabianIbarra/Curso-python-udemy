import os
os.system("cls" if os.name == "nt" else "clear")

# Las keys solo pueden ser inmutables

user = {
    "name": "Fabián",
    "country": "México",
    "email": "fabi_iba4@hotmail.com",
    "age": 24
}

user["city"] = "Culiacán"
print(user["name"])
print(user["country"])
print(user["email"])
print(user["age"])
print(user)