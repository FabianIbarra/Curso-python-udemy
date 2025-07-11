import os
os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        edad = abs(int(input("¿Cuál es tu edad? ")))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

print(f"Tienes {edad} años")
if edad < 18:
    print("Eres menor de edad, no puedes manejar.")
elif edad < 21:
    print("Eres mayor de edad, pero no puedes manejar en algunos estados.")
else:
    print("Eres mayor de edad, puedes manejar.")