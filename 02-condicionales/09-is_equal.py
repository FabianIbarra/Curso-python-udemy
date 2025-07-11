import os
os.system("cls" if os.name == "nt" else "clear")

# == Equal o igualdad y compara valores
# is Equal o identidad y compara en memoria
# Diferencia entre igualdad y identidad
# Comparar valores vs comparar objetos

print(True == 1)  # True
print(True is 1) # False
print(10 == 10.0)  # True
print(10 is 10.0) # False

new_list = []
other_list = []
print(new_list == other_list)  # True
print(new_list is other_list)  # False