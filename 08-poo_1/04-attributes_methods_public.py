import os
os.system("cls" if os.name == "nt" else "clear")

class Person:
    def __init__(self, name, age):
        """Inicializa los atributos de la persona."""
        self.name = name
        self.age = age

    def greet(self):
        """Imprime un saludo personalizado."""
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")
    def eat(self, food):
        """Imprime lo que la persona está comiendo."""
        print(f"{self.name} está comiendo {food}.")

person1 = Person("Fabián", 24)
print(person1.name)
print(person1.age)
person1.greet()
person1.eat("quesadillas")