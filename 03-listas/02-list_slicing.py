import os
os.system("cls" if os.name == "nt" else "clear")

shopping_cart = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry"
]

# [Inicio:Fin:Paso] Genera una nueva lista
shopping_cart.append("fig")
shopping_cart.append("grape")
print(shopping_cart[1:-1:2])
print(shopping_cart)

# Copiar una lista
new_shopping_cart = shopping_cart[:]
new_shopping_cart.append("honeydew")
print(new_shopping_cart)
print(shopping_cart)