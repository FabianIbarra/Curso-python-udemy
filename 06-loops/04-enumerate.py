import os
os.system("cls" if os.name == "nt" else "clear")

# Enumerate: Agrega un contador a un iterable y devuelve pares (índice, valor)
numbers = [1, 2, 3, 4, 5]
for index, number in enumerate(numbers):
    print(f"Index: {index}, Number: {number}")

for index, number in enumerate(list(range(100))):
    print(f"Index: {index}, Number: {number}")