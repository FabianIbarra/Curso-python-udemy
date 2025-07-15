import os
os.system("cls" if os.name == "nt" else "clear")

# Relative path
with open("./fileFolder/relative.txt", mode="r") as my_file:
    print(my_file.readlines())

# Absolute path
with open("C:/Users/Fabián/Desktop/Curso python udemy/13-files/fileFolder/relative.txt", mode="r") as my_file:
    print(my_file.readlines())