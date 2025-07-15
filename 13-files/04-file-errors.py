import os
os.system("cls" if os.name == "nt" else "clear")

try:
    with open("sinpermisos.txt", mode="r") as my_file:
        print(my_file.readlines())
except FileNotFoundError:
    print("El archivo no existe. Por favor, verifica el nombre del archivo.")