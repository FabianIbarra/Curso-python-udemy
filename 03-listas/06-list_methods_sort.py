import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos de ordenamiento

letters = ["a", "n", "o", "z", "y", "b", "c", "d"]

# sorted()
new_letters = sorted(letters)
print(new_letters)
print(letters)

# sort()
letters.sort()
print(letters)

# Reverse
letters.reverse()
print(letters)