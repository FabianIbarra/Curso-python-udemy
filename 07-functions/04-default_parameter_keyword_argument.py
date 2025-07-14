import os
os.system("cls" if os.name == "nt" else "clear")

# Funciones con parámetros por defecto y argumentos por palabra clave
# Parámetros por defecto: Permiten definir valores predeterminados para los parámetros de una función
def greet(greet="Hola", name="Fabián"):
    """Imprime un saludo personalizado con parámetros por defecto."""
    print(f"{greet}, {name}!")

greet()  # Usa los valores por defecto
greet("Buenos días")  # Cambia el saludo, pero usa el nombre por defecto