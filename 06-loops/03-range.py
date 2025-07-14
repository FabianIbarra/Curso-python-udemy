import os
os.system("cls" if os.name == "nt" else "clear")

print(range(0, 10))  # range(start, stop)
# print(iter(range(0, 10)))  # Convert range to an iterator

for number in range(0, 100, 3):
    print(number)