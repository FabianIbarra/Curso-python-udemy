import os
os.system("cls" if os.name == "nt" else "clear")

is_student = True

# if is_student:
#     print("Licencia de estudiante")
# else:
#     print("Licencia normal")

# True if condition else False

get_license = "Licencia de estudiante" if is_student else "Licencia normal"
print(get_license)