import os
os.system("cls" if os.name == "nt" else "clear")

# Dunder Methods: Métodos especiales que permiten definir el comportamiento de los objetos

class Person:
    def __init__(self, name, age):
        """Inicializa el nombre y la edad de la persona."""
        self.name = name
        self.age = age

    def __str__(self):
        """Representación en cadena del objeto."""
        return f"{self.name}, {self.age} años"
    
    def __len__(self):
        """Devuelve la longitud del nombre de la persona."""
        return len(self.name)

    def __eq__(self, other):
        """Compara dos objetos Person por nombre y edad."""
        return self.name == other.name and self.age == other.age
    
persona = Person("Juan", 30)
print(persona)
print(len(persona))