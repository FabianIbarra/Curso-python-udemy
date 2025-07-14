import os
os.system("cls" if os.name == "nt" else "clear")

#  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  numeros = "0123456789"
#  simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
# caracteres = letras + numeros + simbolos
# Formula simple: (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Salida : &D^#23SN

import string
import random

def password_generator(length=8):
    """Genera una contraseña aleatoria de una longitud específica."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(length))
    return password

print(password_generator(5))