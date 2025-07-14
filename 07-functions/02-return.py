import os
os.system("cls" if os.name == "nt" else "clear")

# Funciones: Bloques de código reutilizables que realizan una tarea específica
def greet(name):
    """Imprime un saludo personalizado."""
    print(f"Hola, {name}!")
    return "Hola desde return"

def add(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

print(greet("Fabián"))
result = add(5, 3)
print(f"La suma es: {result}")