import os
os.system("cls" if os.name == "nt" else "clear")

# Object-Oriented Programming (OOP): Paradigma de programación que utiliza "objetos" para encapsular datos y comportamientos.
# Objetos: Instancias de clases que contienen atributos y métodos.
class Car:
    def __init__(self, make, model, year):
        """Inicializa los atributos del coche."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Muestra la información del coche."""
        print(f"Coche: {self.year} {self.make} {self.model}")

# Creación de una instancia de la clase Car
my_car = Car("Toyota", "Corolla", 2020)

# Llamada al método para mostrar la información del coche
my_car.display_info()