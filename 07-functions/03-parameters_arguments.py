import os
os.system("cls" if os.name == "nt" else "clear")

# Parámetros y argumentos: Definición de funciones con parámetros y su uso al llamar a la función
# Parámetros: Variables definidas en la función
def greet(name):
    """Imprime un saludo personalizado."""
    print(f"Hola, {name}!")

# Argumentos: Valores pasados a la función al llamarla
greet("Fabián")