import os
os.system("cls" if os.name == "nt" else "clear")

# Polimorfismo: Permite que diferentes clases implementen métodos con el mismo nombre

class Animal:
    def sound(self):
        """Método genérico para el sonido del animal."""
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        """Implementación del sonido específico de un perro."""
        return "¡Guau!"

class Cat(Animal):
    def sound(self):
        """Implementación del sonido específico de un gato."""
        return "¡Miau!"
    
def make_sound(animal):
    """Función que recibe un animal y llama a su método sound."""
    print(animal.sound())

def make_noise(animal):
    """Función que recibe un animal y llama a su método sound."""
    if isinstance(animal, Animal):
        make_sound(animal)
    else:
        print("El objeto no es un Animal")

jake = Dog()
whiskers = Cat()
make_noise(jake)
make_noise(whiskers)
make_noise("serpiente")