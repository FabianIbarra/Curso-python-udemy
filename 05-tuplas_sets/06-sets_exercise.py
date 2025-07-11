import os
os.system("cls" if os.name == "nt" else "clear")

python_course = {"Ana", "Luis", "Pedro", "Beto", "Lucia"}
java_course = {"Pedro", "Juan", "Mario", "Beto", "Armando"}

# .intersection()
print(python_course.intersection(java_course))

# .union()
print(python_course.union(java_course))

# .difference()
print(python_course.difference(java_course))

