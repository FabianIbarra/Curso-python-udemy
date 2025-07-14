import os
os.system("cls" if os.name == "nt" else "clear")

# Herencia: Permite que una clase herede atributos y métodos de otra clase
class Animal:
    def __init__(self, name):
        """Inicializa el nombre del animal."""
        self.name = name

    def sleep(self):
        """Imprime un sonido genérico del animal."""
        print(f"{self.name} está durmiendo.")

class Dog(Animal):
    def dog_sound(self):
        """Imprime el sonido específico de un perro."""
        print(f"{self.name} dice: ¡Guau!")

class Cat(Animal):
    def cat_sound(self):
        """Imprime el sonido específico de un gato."""
        print(f"{self.name} dice: ¡Miau!")

firulais = Dog("Firulais")
miau = Cat("Miau")
firulais.sleep()
firulais.dog_sound()
miau.sleep()
miau.cat_sound()