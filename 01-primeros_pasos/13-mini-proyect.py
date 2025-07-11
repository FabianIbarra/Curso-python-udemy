# Recibe de forma diámica el nombre, año de nacimiento, correo y contraseña del usuario.
# Imprime un mensaje de bienvenida con los datos ingresados.
import os
os.system("cls" if os.name == "nt" else "clear")
# Solicitar datos al usuario
name = input("Ingrese su nombre: ")
while True:
    try:
        year = int(input("Ingrese su año de nacimiento: "))
        break
    except ValueError:
        print("Por favor, ingrese un año válido (número entero).")
email = input("Ingrese su correo electrónico: ")
password = input("Ingrese su contraseña: ")

# Imprimir mensaje de bienvenida
# print(f"\nBienvenido {name}!")
# print(f"Tu correo electrónico es: {email}")
# print(f"En el 2050 tendrás {2050 - int(year)} años.")
# password_length = len(password)
# # if password_length == 0:
# #     print(f"No tienes contraseña")
# # else:
# #     for i in range(password_length):
# #         password = password.replace(password[i], "*")
# #     print(f"Tu contraseña es: {password}"
# if password_length == 0:
#     print("No tienes contraseña")
# else:
#     print(f"Tu contraseña es: {'*' * password_length}")
if len(password) == 0:
    print(f"""
        Bienvenido {name}!
        Tu correo electrónico es: {email}
        En el 2050 tendrás {2050 - year} años.
        No tienes contraseña.
    """)
else:
    print(f"""
        Bienvenido {name}!
        Tu correo electrónico es: {email}
        En el 2050 tendrás {2050 - year} años.
        Tu contraseña es: {'*' * len(password)}
    """)