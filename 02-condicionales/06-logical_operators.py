import os
os.system("cls" if os.name == "nt" else "clear")

# Evluar condiciones lógicas
# Operadores lógicos: and, or, not
# # and: verdadero si ambas condiciones son verdaderas

# print(True and True)  # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False)  # False

# # or: verdadero si al menos una condición es verdadera

# print(True or True)  # True
# print(True or False)  # True
# print(False or True)  # True
# print(False or False)  # False

# # not: invierte el valor de verdad
# print(not True)  # False
# print(not False)  # True
# print(not (True and False))  # True
# print(not (False or True))  # False
# print(not (False and False))  # True

# and

age = 25
licensed = True

print("Puedes manejar") if age >= 18 and licensed else print("Espera a cumplir la mayoría de edad o trámita tu licencia.")

# or

is_student = False
membership = True

print("Obten la licencia de estudiante") if is_student or membership else print("No puedes obtener la licencia de estudiante")

# not

is_admin = True

print("Acceso concedido") if not is_admin else print("Acceso denegado")