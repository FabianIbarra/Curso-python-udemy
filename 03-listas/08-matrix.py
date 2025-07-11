import os
os.system("cls" if os.name == "nt" else "clear")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][0])
matrix[1][0] = 10
print(matrix)