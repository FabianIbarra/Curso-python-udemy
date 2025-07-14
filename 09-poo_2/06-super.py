import os
os.system("cls" if os.name == "nt" else "clear")

# super(): Función que permite llamar a métodos de la clase padre desde una clase hija en programación orientada a objetos (POO).
class Animal:
    def __init__(self, name, age):
        """Inicializa el nombre del animal."""
        self.name = name
        self.age = age

    def sound(self):
        """Imprime un sonido genérico del animal."""
        print(f"{self.name} hace un sonido.")

    def info(self):
        """Muestra la información del animal."""
        print(f"Nombre: {self.name}, Edad: {self.age} años")

class Dog(Animal):
    def __init__(self, name, age, breed):
        """Inicializa el nombre y la edad del perro."""
        super().__init__(name, age)  # Llama al constructor de la clase padre
        self.breed = breed

    def sound(self):
        """Imprime el sonido específico de un perro."""
        super().sound()  # Llama al método de la clase padre
        print(f"{self.name} dice: ¡Guau!")

    def info(self):
        """Muestra la información del perro."""
        super().info()
        print(f"Raza: {self.breed}")

class Cat(Animal):
    def __init__(self, name, age, breed):
        """Inicializa el nombre y la edad del gato."""
        super().__init__(name, age)  # Llama al constructor de la clase padre
        self.breed = breed

    def sound(self):
        """Imprime el sonido específico de un gato."""
        super().sound()
        print(f"{self.name} dice: ¡Miau!")

firulais = Dog("Firulais", 2, "Labrador")
miau = Cat("Miau", 1, "Siames")
firulais.info()
firulais.sound()
miau.sound()