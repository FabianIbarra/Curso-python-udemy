import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos de sets en teoría de conjuntos

# .union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# .intersection()
print(set1.intersection(set2))

# .difference
print(set1.difference(set2))

# .symmetric_difference()
print(set1.symmetric_difference(set2))