import os
os.system("cls" if os.name == "nt" else "clear")

# Igualdad ==

print(5 == 5)  # True
print(5 == 3)  # False
print("hello" == "hello")  # True

# Desigualdad !=

print(5 != 3)  # True
print(5 != 5)  # False
print("hello" != "world")  # True

# Mayor que >

print(5 > 3)  # True
print(3 > 5)  # False
print(5 > 5)  # False

# Menor que <

print(3 < 5)  # True
print(5 < 3)  # False
print(5 < 5)  # False

# Mayor o igual que >=

print(5 >= 5)  # True
print(5 >= 3)  # True
print(3 >= 5)  # False

# Menor o igual que <=

print(3 <= 5)  # True
print(5 <= 5)  # True
print(5 <= 3)  # False