import os
os.system("cls" if os.name == "nt" else "clear")

# Conjuntos

# .add()
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
print(my_set)

# .update()
my_set.update([7, 8, 9])
print(my_set)

# .remove(): Marca error si el dato no se encuentra en el set
my_set.remove(9)
print(my_set)

# .discard(): No marca error si no existe el dato que quieres eliminar
my_set.discard(8)
print(my_set)

# .pop(): Elimina un dato al azar
print(my_set.pop())
print(my_set)

# .clear(): Elimina todos los datos del set
my_set.clear()
print(my_set)

# del: Elimina el objeto set
del my_set