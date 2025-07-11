import os
os.system("cls" if os.name == "nt" else "clear")

list1 = [1, 2, 3, 4, 5, 4, 3, 4, 1, 3]
tuple1 = tuple(list1)
print(list1)
print(tuple1)
print(type(tuple1))
set1 = set(list1)
print(set1)
print(type(set1))

list_tuple = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(list_tuple)
print(list_tuple)
print(dictionary)
print(type(dictionary))