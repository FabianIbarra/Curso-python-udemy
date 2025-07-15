import os
os.system("cls" if os.name == "nt" else "clear")

# Toda la librería
import math
print(math.sqrt(16))

# Importación de un módulo específico
from datetime import datetime
print(datetime.now())

# Importación de un módulo con alias
import random as rnd
print(rnd.randint(1, 10))

# Importación de funciones específicas
from math import pi, sin
print(f"Valor de pi: {pi}")
print(f"Seno de 0: {sin(0)}")

# Importación de todo el contenido de un módulo (no recomendado en producción)
from math import *
print(f"Coseno de 0: {cos(0)}")