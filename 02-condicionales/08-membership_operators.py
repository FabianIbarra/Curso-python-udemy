import os
os.system("cls" if os.name == "nt" else "clear")

# in

print("a" in "hola")  # True
print("b" in "hola")  # False
print(9 in range(10))  # True
print(10 in range(10))  # False

# not in

print("a" not in "hola")  # False
print("b" not in "hola")  # True
print(9 not in range(10))  # False
print(10 not in range(10))  # True

fruits = ["apple", "banana", "cherry"]

# in with lists

print("apple" in fruits)  # True
print("orange" not in fruits)  # True