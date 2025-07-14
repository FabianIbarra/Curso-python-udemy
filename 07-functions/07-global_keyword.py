import os
os.system("cls" if os.name == "nt" else "clear")

# Global Keyword: Permite modificar una variable global dentro de una función
tax = 16

def change_global():
    """Modifica la variable global tax."""
    global tax  # Indica que se usará la variable global tax
    tax = 20  # Cambia el valor de la variable global
    return tax

print(change_global())  # Imprime el nuevo valor de tax
print(f"Valor original de tax: {tax}")  # Imprime el valor original