import os
os.system("cls" if os.name == "nt" else "clear")

# Errores personalizados: Definición de excepciones personalizadas

class InvalidAgeError(Exception):
    """Excepción personalizada para edades inválidas."""
    def __init__(self, age, message="La edad debe ser mayor o igual a 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)

def register_user(name, age):
    """Registra un usuario si la edad es válida."""
    if age < 18:
        raise InvalidAgeError(age)
    print(f"Usuario {name} registrado con éxito.")

try:
    register_user("Juan", 16)
except InvalidAgeError as e:
    print(f"Error: {e.message} Edad proporcionada: {e.age}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Registro exitoso.")
finally:
    print("Proceso de registro finalizado.")