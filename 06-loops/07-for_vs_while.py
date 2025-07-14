import os
os.system("cls" if os.name == "nt" else "clear")

# For Loop: para iterables como listas, tuplas, diccionarios, etc, cuando
# se conoce el número de iteraciones
# While Loop: Cuando no se conoce el número de iteraciones y necesita una condición

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(f"Item: {item}")

item = 0
while item < len(my_list):
    print(f"Item: {my_list[item]}")
    item += 1
