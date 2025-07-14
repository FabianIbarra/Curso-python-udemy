import os
os.system("cls" if os.name == "nt" else "clear")

# Break: Termina el bucle inmediatamente
cont = 0
while True:
    if cont > 5:
        break
    print(f"Contador: {cont}")
    cont += 1

# Continue: Salta a la siguiente iteración del bucle
cont = 0
while cont < 10:
    cont += 1
    if cont % 2 == 0:  # Si es par, saltar a la siguiente iteración
        continue
    print(f"Contador impar: {cont}")

# Pass: No hace nada, se usa como marcador de posición
cont = 0
while cont < 5:
    pass  # Aquí podría ir código en el futuro
    cont += 1
else:
    print("Bucle while con pass completado.")