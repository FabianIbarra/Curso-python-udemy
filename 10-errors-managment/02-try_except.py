import os
os.system("cls" if os.name == "nt" else "clear")

# Try/Except: Manejo de excepciones para evitar que el programa se detenga

def divide_numbers():
    try:
        a = int(input("Ingrese el numerador: "))
        b = int(input("Ingrese el denominador: "))
        result = a / b
        print(f"Resultado: {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Los valores deben ser números.")
    except Exception as e:
        print(f"Error inesperado: {e}")

divide_numbers()