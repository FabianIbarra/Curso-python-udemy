import os
os.system("cls" if os.name == "nt" else "clear")

# Funciones: Bloques de código reutilizables que realizan una tarea específica
def greet(name):
    """Imprime un saludo personalizado."""
    print(f"Hola, {name}!")

greet("Fabián")