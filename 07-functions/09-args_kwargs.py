import os
os.system("cls" if os.name == "nt" else "clear")

# args: Permiten pasar un número variable de argumentos a una función
def print_args(*args):
    """Imprime los argumentos pasados a la función."""
    for arg in args:
        print(arg)
# Llamada a la función con múltiples argumentos
print_args("Fabián", 24, "México")

# kwargs: Permiten pasar un número variable de argumentos a una función como un diccionario
def print_info(**kwargs):
    """Imprime información pasada como argumentos de palabra clave."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Llamada a la función con argumentos de palabra clave
print_info(name="Fabián", age=24, city="México")