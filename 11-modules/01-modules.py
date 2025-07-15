import os
os.system("cls" if os.name == "nt" else "clear")

# Modulos: Importación de módulos y uso de funciones

from math_utils import addition # Defined module: es un módulo personalizado.

result = addition(5, 3)
print(f"La suma de 5 y 3 es: {result}")