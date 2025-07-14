import os
os.system("cls" if os.name == "nt" else "clear")

# Composición: Relación "tiene un" entre clases, donde una clase contiene instancias de otra
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
    def __init__(self):
        """Inicializa el pato."""
        self.flyer = Flyer()
        self.swimmer = Swimmer()

    def quack(self):
        """Método que simula el sonido de un pato."""
        print("¡Cuac! ¡Cuac!")

    def start_flying(self):
        """Inicia el vuelo del pato."""
        self.flyer.fly()

    def start_swimming(self):
        """Inicia la natación del pato."""
        self.swimmer.swim()

donald = Duck()
donald.start_flying()
donald.start_swimming()
donald.quack()
donald.do_something()