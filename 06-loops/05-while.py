import os
os.system("cls" if os.name == "nt" else "clear")

# While Loop: Repite un bloque de código mientras una condición sea verdadera
cont = 0
while cont <= 5:
    print(f"Contador: {cont}")
    cont += 1
else:
    print("El contador ha llegado a 6, saliendo del bucle.")

# Solicitar al usuario que escriba 'exit' para salir del bucle
response = ''

while response.lower() != 'exit':
    response = input("Escribe 'exit' para salir: ")
    if response.lower() == 'exit':
        print("Saliendo del bucle.")
    else:
        print(f"Has escrito: {response}")