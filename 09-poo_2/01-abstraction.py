import os
os.system("cls" if os.name == "nt" else "clear")

# Abstracción: Oculta los detalles de implementación y muestra solo la funcionalidad esencial
class CoffeeMaker:
    def __init__(self, brand, model):
        """Inicializa los atributos de la cafetera."""
        self.brand = brand
        self.model = model
    def make_coffee(self):
        """Simula el proceso de hacer café."""
        self.__boil_water()
        self.__mix()
        print(f"Tu café está listo.")
    
    def __boil_water(self):
        """Método privado que simula hervir agua."""
        print(f"Herviendo agua en la {self.brand} {self.model}...")

    def __mix(self):
        """Método privado que simula mezclar el café."""
        print(f"Mezclando café en la {self.brand} {self.model}...")

coffee_maker = CoffeeMaker("Nespresso", "Essenza Mini")
coffee_maker.make_coffee()  # Llama al método público que hace el café