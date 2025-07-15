import os
os.system("cls" if os.name == "nt" else "clear")

# Paquetes: Importación de paquetes y uso de funciones
from my_package import addition, greet, bye

print(addition(6, 7, 5, 8, 4, 7, 6))
greet("Fabián")
bye("Fabián")