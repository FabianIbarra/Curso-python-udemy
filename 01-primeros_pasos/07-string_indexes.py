import os
os.system("cls" if os.name == "nt" else "clear")
# ctrl + k + c: para comentar una línea
# ctrl + k + u: para descomentar una línea
name = "Fabián"
print(name[0])  # Imprime la primera letra
print(name[1])  # Imprime la segunda letra
print(name[2])  # Imprime la tercera letra
print(name[3])  # Imprime la cuarta letra
print(name[4])  # Imprime la quinta letra
print(name[-1])  # Imprime la última letra

# [Start:Stop:Stepover]
print(name[:4])
print(name[::2])

# ¿Cómo puedo poner mi nombre al revés?
name = "Fabián"
print(name[::-1])