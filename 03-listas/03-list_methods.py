import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos de adición
# Append

numbers_list = list(range(1, 11))
print(numbers_list)
numbers_list.append(11)
print(numbers_list)

# Insert

numbers_list.insert(1, 90)
print(numbers_list)

# Extends

numbers_list.extend([12, 13, 14])
print(numbers_list)