import os
os.system("cls" if os.name == "nt" else "clear")

# Constructores: Métodos especiales que se ejecutan al crear una instancia de una clase
class Car:
    def __init__(self, make, model, year):
        """Inicializa los atributos del coche."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Muestra la información del coche."""
        print(f"Coche: {self.year} {self.make} {self.model}")