import os
os.system("cls" if os.name == "nt" else "clear")

import csv

with open("datos.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Edad", "Ciudad"])
    writer.writerow(["Alice", 30, "Nueva York"])
    writer.writerow(["Bob", 25, "Los Ángeles"])

with open("datos.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)