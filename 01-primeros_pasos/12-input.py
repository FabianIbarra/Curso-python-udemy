import os
os.system("cls" if os.name == "nt" else "clear")

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = input("Ingrese su edad: ")
print(f"Hola, mi nombre es {name} {last_name} y tengo {age} años.")