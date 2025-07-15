import os
os.system("cls" if os.name == "nt" else "clear")

my_file = open("test.txt")
# print(my_file.read())

# # seek
# my_file.seek(4)  # Regresa al inicio del archivo
# print(my_file.read())

# readline
print(my_file.readline())  # Lee una línea del archivo
print(my_file.readline())  # Lee otra línea del archivo
print(my_file.readlines())  # Lee otra línea del archivo

my_file.close()