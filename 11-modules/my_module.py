import os
os.system("cls" if os.name == "nt" else "clear")

# __name__: Módulo principal y ejecución de código

def greet():
    """Imprime un saludo personalizado."""
    print(f"Hola desde modulo")

if __name__ == "__main__":
    print("Este es el módulo principal.")
    greet()

print("El nombre del módulo es:", __name__)