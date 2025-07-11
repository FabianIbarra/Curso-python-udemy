import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos de sets en teoría de conjuntos

set1 = {3, 9}
set2 = {3, 4, 5, 7, 9}

# .issubset()
print(set1.issubset(set2))

# .issuperset
print(set1.issuperset(set2))