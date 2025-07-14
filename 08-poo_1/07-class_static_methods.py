import os
os.system("cls" if os.name == "nt" else "clear")

class Person:
    species = "Humano"

    def __init__(self, name, age):
        """Inicializa los atributos de la persona."""
        self.name = name
        self.age = age

    @classmethod
    def change_spiecies(cls, new_specie):
        """Cambia la especie de la persona."""
        cls.species = new_specie
        print(f"Ahora es un {cls.species}.")
    @staticmethod
    def is_older(age):
        """Verifica si la persona es mayor de edad."""
        return age >= 18

person1 = Person("Fabián", 24)
print(f"{person1.name} es un {person1.species}.")
person1.change_spiecies("Extraterrestre")

person2 = Person("Ana", 30)
print(f"{person2.name} es un {person2.species}.")

print(Person.is_older(15))
print(person1.is_older(person1.age))