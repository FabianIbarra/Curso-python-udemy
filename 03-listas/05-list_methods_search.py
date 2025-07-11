import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos de búsqueda

# Count

numbers_list = list(range(1, 11))
print(numbers_list)

numbers_list.append(3)

print(numbers_list.count(3))

# Index

print(numbers_list.index(5))

# In

print(5 in numbers_list)

# Sort

numbers_list.sort()
print(numbers_list)

# Reverse

numbers_list.reverse()
print(numbers_list)