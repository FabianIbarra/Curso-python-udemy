import os
os.system("cls" if os.name == "nt" else "clear")

class BankAccount:
    """Clase que representa una cuenta bancaria."""
    interest_rate = 0.05
    
    def __init__(self, holder, balance=0):
        """Inicializa los atributos de la cuenta bancaria."""
        self.holder = holder
        self.balance = balance

    @classmethod
    def change_interest_rate(cls, new_rate):
        """Cambia la tasa de interés de la cuenta bancaria."""
        cls.interest_rate = new_rate
        print(f"Tasa de interés actualizada a {cls.interest_rate * 100}%.")
    
    @staticmethod
    def is_valid_amount(amount):
        """Verifica si el monto es válido (no negativo)."""
        return amount >= 0
    
    def wiithdraw(self, amount):
        """Retira una cantidad de la cuenta bancaria."""
        if self.is_valid_amount(amount) and amount <= self.balance:
            self.balance -= amount
            print(f"Retirado: {amount}. Nuevo saldo: {self.balance}.")
        else:
            print("Monto inválido o saldo insuficiente.")

account1 = BankAccount("Fabián", 1000)
account2 = BankAccount("Ana", 500)

print(BankAccount.interest_rate)
BankAccount.change_interest_rate(0.07)
print(BankAccount.interest_rate)

account1.wiithdraw(200)
account2.wiithdraw(600)

print(BankAccount.is_valid_amount(100))

# Función vs Método
# Una función es un bloque de código independiente, mientras que un método es una función asociada a una clase.
# Los métodos pueden acceder a los atributos de la instancia y de la clase, mientras que las funciones no.