import os
os.system("cls" if os.name == "nt" else "clear")

is_old = False
is_licensed = False

if is_old:
    print("Puedes manejar")
elif is_licensed:
    print("Puedes manejar con tu licencia en la ciudad.")
else:
    print("Espera a cumplir la mayoría de edad o trámita tu licencia.")