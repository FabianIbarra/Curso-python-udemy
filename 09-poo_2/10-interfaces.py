import os
os.system("cls" if os.name == "nt" else "clear")

# Interfaces: Definición de métodos que deben ser implementados por las clases que heredan de la interfaz

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

# animal = Animal()  # Esto fallará porque Animal es abstracto

class Dog(Animal):
    def sound(self):
        """Método abstracto que debe ser implementado por las subclases."""
        return "¡Guau!"

class Cat(Animal):
    def sound(self):
        """Método abstracto que debe ser implementado por las subclases."""
        return "¡Miau!"

taquito = Dog()
print(taquito.sound())
michifus = Cat()
print(michifus.sound())