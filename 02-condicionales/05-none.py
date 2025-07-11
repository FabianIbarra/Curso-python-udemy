import os
os.system("cls" if os.name == "nt" else "clear")

# None es un valor especial en Python que representa la ausencia de valor o un valor nulo (Null == None).
print(bool(None))

user = None
print(type(user))

if user:
    print("El usuario está registrado")
else:
    print("Usuario disponible")