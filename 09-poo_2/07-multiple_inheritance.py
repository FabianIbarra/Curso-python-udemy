import os
os.system("cls" if os.name == "nt" else "clear")

# Herencia Múltiple: Permite que una clase herede de múltiples clases base
class Flyer:
    """Clase base para objetos voladores."""
    def fly(self):
        """Método que simula el vuelo."""
        print("Puedo volar alto en el cielo.")
    
    def do_something(self):
        """Método que simula un salto mortal."""
        print("Hago un salto mortal en el aire.")   

class Swimmer:
    """Clase base para objetos nadadores."""
    def swim(self):
        """Método que simula la natación."""
        print("Puedo nadar en el agua.")
    
    def do_something(self):
        """Método que simula un giro en el agua."""
        print("Hago un giro en el agua.")

class Duck(Flyer, Swimmer):
    """Clase que representa un pato, que puede volar y nadar."""
    def quack(self):
        """Método que simula el sonido de un pato."""
        print("¡Cuac! ¡Cuac!")

donald = Duck()
donald.fly()   # Llama al método de la clase Flyer
donald.swim()  # Llama al método de la clase Swimmer
donald.quack()  # Llama al método específico de la clase Duck
donald.do_something()  # Llama al método de la clase Flyer, ya que es el primero en la jerarquía de herencia

# MRO (Method Resolution Order)
print(Duck.__mro__)  # Muestra el orden de resolución de métodos para la clase Duck