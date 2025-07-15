import os
os.system("cls" if os.name == "nt" else "clear")

with open("test.txt", mode="r") as my_file:
    print(my_file.readlines())

with open("archivo.txt", mode="w") as my_file:
    text = my_file.write(":)")

with open("test.txt", mode="r+") as my_file:
    print(my_file.readlines())
    text = my_file.write("\nHola, Python!")

with open("test.txt", mode="a") as my_file:
    text = my_file.write("123")
    print(text)