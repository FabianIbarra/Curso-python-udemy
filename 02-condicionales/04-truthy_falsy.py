import os
os.system("cls" if os.name == "nt" else "clear")

# Truthy (Verdaderos) y Falsy (Falsos)
print(bool(True))
print(bool(1))  # Verdadero
print(bool(0))  # Falso
print(bool("Hola"))  # Verdadero
print(bool(None))  # Falso