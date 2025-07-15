import os
os.system("cls" if os.name == "nt" else "clear")

from cowpy import cow
# Uso de la biblioteca cowpy para imprimir un mensaje divertido
vaca = cow.Cowacter()
print(vaca.milk("¡Hola, Python!"))