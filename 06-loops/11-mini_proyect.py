import os
os.system("cls" if os.name == "nt" else "clear")

# Diccionario del inventario en una dulcería
inventory = {
    "chocolate": 10,
    "caramelos": 5,
    "golosinas": 15,
    "chicles": 2,
    "gominolas": 8,
    "paletas": 4,
    "piruletas": 5,
    "bombones": 20,
}

cart = []
opcion = ""
total = 0

while opcion != 0:
    try:
        print("Bienvenido a la dulcería. Aquí está nuestro inventario:")
        for index, value in enumerate(inventory.items()):
            print(f"{index+1}. {value[0].capitalize()}: ${value[1]} pesos.")
        print("\n¿Qué dulce te gustaría comprar? (Ingresa el número del dulce o 0 para salir):")
        opcion = int(input("Dulce: "))
        match opcion:
            case opcion if 1 <= opcion <= len(inventory):
                item = list(inventory.keys())[opcion - 1]
                if inventory[item] > 0:
                    cart.append(item)
                    print(f"Has agregado {item} al carrito.")
                else:
                    print(f"Lo siento, {item} está agotado.")
            case 0:
                print("Productos en tu carrito:")
                if cart:
                    for product in cart:
                        print(f"- {product.capitalize()}")
                        total += inventory[product]
                    print(f"Tu carrito tiene un costo de ${total} pesos. Gracias por tu visita.")
                else:
                    print("Tu carrito está vacío.")
            case _:
                print("Opción inválida. Por favor, elige un número válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
