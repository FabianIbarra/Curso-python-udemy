import os
os.system("cls" if os.name == "nt" else "clear")

students = {
    "Ana": [8, 7.7, 9],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}

# Agregar nuevo estudiante
# Sacar el promedio de un estudiante existente
# El promedio del estudiante nuevo

students["Fabián"] = [10, 9, 10, 8, 7]
print(students)

print(f"El prmedio de Ana es: {(sum(students["Ana"]) / len(students["Ana"])):.2f}") if "Ana" in students else print("No existe el estudiante")
print(f"El prmedio de Fabián es: {(sum(students["Fabián"]) / len(students["Fabián"])):.2f}")