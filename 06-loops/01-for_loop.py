import os
os.system("cls" if os.name == "nt" else "clear")

for item in 'Python':
    print(item)

fruits = ["manzanas", "platanos", "peras"]
for fruit in fruits:
    print(fruit)

my_list = [1, 2, 3, 4, 5]
sum = 0
for number in my_list:
    print(number)
    sum += number

print(sum)