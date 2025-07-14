import os
os.system("cls" if os.name == "nt" else "clear")

# Clase abstracta: No se puede instanciar directamente, sirve como base para otras clases
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

# animal = Animal()  # Esto fallará porque Animal es abstracto