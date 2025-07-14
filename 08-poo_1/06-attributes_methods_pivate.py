import os
os.system("cls" if os.name == "nt" else "clear")

# Métodos privados: Métodos que no deben ser accedidos desde fuera de la clase, se indican con un guion bajo al inicio
class Person:
    def __init__(self, name, age):
        """Inicializa los atributos de la persona."""
        self.name = name
        self.age = age
        self.__password = '1234'    # atributo privado (name mangling:
                                    # se cambia el nombre para evitar conflictos)

    def __generate_password(self):
        """Método privado que genera una contraseña."""
        self.__password = f"{self.name}{self.age}"
        return self.__password
    
person1 = Person("Fabián", 24)
print(person1._Person__password)  # Intento de acceso al atributo privado (no recomendado)
# print(person1.__generate_password())  # Esto fallará porque el método es privado
print(person1._Person__generate_password())  # Acceso al método privado usando name mangling
print(person1._Person__password)