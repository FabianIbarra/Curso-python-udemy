import os
os.system("cls" if os.name == "nt" else "clear")

class Person:
    def __init__(self, name, age):
        """Inicializa los atributos de la persona."""
        self.name = name # atributo de instancia
        self.age = age
        self._energy = 100 # atributo protegido

    def _waste_energy(self, quantity):
        """Método protegido que simula el desperdicio de energía."""
        print(f"{self.name} está desperdiciando {quantity} unidades de energía.")
        self._energy -= quantity

person1 = Person("Fabián", 24)
print(person1.name)  # Acceso al atributo público
person1._waste_energy(20)  # Acceso al método protegido
print(person1._energy)  # Acceso al atributo protegido, aunque no es recomendado porque es una convención
# Nota: Los atributos y métodos protegidos se indican con un guion bajo al inicio,
# pero aún son accesibles desde fuera de la clase. Se recomienda no acceder a ellos directamente.