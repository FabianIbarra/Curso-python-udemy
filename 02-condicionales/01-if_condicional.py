import os
os.system("cls" if os.name == "nt" else "clear")

# is_old = False

# if is_old:
#     print("Puedes manejar")
# else:
#     print("Espera a cumplir la mayoría de edad")

is_student = True

if is_student:
    print("Obten la licencia de estudiante")
else:
    print("No puedes obtener la licencia de estudiante")