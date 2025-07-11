import os
os.system("cls" if os.name == "nt" else "clear")

# ¿Qué es inmutabilidad?
# Las cadenas de texto (strings) en Python son inmutables, lo que significa que no se pueden modificar una vez creadas.
# Si intentas cambiar un carácter en una cadena, obtendrás un error.

nombre = "Fabián"
try:
    nombre[0] = "B"  # Esto generará un error
except TypeError as e:
    print(f"Error: Las cadenas de texto son inmutables. {e}")
nombre = "Fabián Ibarra"
print(nombre)