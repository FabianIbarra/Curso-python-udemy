import os
os.system("cls" if os.name == "nt" else "clear")

# Encapsulación: Agrupa datos y comportamientos relacionados en una clase, ocultando detalles internos

class BankAccount:
    def __init__(self, account_number, balance=0):
        """Inicializa los atributos de la cuenta bancaria."""
        self.account_number = account_number
        self.__balance = balance  # Atributo privado

    def deposit(self, amount):
        """Deposita una cantidad en la cuenta."""
        if amount > 0:
            self.__balance += amount
            print(f"Depositado: {amount}. Nuevo saldo: {self.__balance}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def withdraw(self, amount):
        """Retira una cantidad de la cuenta."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Retirado: {amount}. Nuevo saldo: {self.__balance}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def get_balance(self):
        """Devuelve el saldo actual de la cuenta."""
        return self.__balance
    
account = BankAccount("123456789", 1000)
account.deposit(500)
print(f"Saldo actual: {account.get_balance()}")  # Acceso al saldo a través de un método público