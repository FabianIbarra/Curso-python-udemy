import os
os.system("cls" if os.name == "nt" else "clear")

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Ordenada
# INMUTABLES: No se pueden modificar
# Permite duplicados
# Indexadas

# Métodos
# .count()
print(my_tuple.count(1))
# .index()
print(my_tuple.index(3))

week = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")