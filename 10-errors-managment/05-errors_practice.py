import os
os.system("cls" if os.name == "nt" else "clear")

# Errores personalizados: Definición de excepciones personalizadas

class InvalidAgeError(Exception):
    """Excepción personalizada para edades inválidas."""
    def __init__(self, age, message="La edad debe ser mayor o igual a 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InvalidEmailError(Exception):
    """Excepción personalizada para correos electrónicos inválidos."""
    def __init__(self, email, message="El correo electrónico es inválido."):
        self.email = email
        self.message = message
        super().__init__(self.message)

def register_user(name, age, email):
    """Registra un usuario si la edad es válida."""
    if age < 18:
        raise InvalidAgeError(age)
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError(email)
    print(f"Usuario {name} registrado con éxito con la edad {age} y el correo {email}.")

try:
    register_user("Juan", 18, "fabi@hotmail.com")
except InvalidAgeError as e:
    print(f"Error: {e.message} Edad proporcionada: {e.age}")
except InvalidEmailError as e:
    print(f"Error: {e.message} Correo proporcionado: {e.email}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Registro exitoso.")
finally:
    print("Proceso de registro finalizado.")