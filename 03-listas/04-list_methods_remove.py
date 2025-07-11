import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos de eliminación

numbers_list = list(range(1, 11))
print(numbers_list)

# Pop

print(numbers_list.pop())
print(numbers_list)

print(numbers_list.pop(0))
print(numbers_list)

# Remove

numbers_list.remove(5)
print(numbers_list)

# Clear

numbers_list.clear()
print(numbers_list)