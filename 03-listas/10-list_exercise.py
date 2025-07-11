import os
os.system("cls" if os.name == "nt" else "clear")

# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
while True:
    try:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Carrito de compras")
        print("Opciones: ")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar la lista ordenada")
        print("4. Buscar producto")
        print("5. Contar productos del carrito")
        print("6. Vaciar el carrito")
        print("7. Salir")
        option = int(input("Elige una opción (1-7): "))
        match option:
            case 1:
                print("Agregar producto")
                product = input("Ingresa el nombre del producto: ").title()
                shopping_cart.append(product)
                print(f"El producto {product} ha sido agregado al carrito.")
            case 2:
                print("Eliminar producto")
                product = input("Ingresa el nombre del producto a eliminar: ").title()
                shopping_cart.remove(product)
                print(f"El producto {product} ha sido eliminado del carrito.")
            case 3:
                print("Mostrar la lista ordenada")
                if len(shopping_cart) == 0:
                    print("El carrito está vacío.")
                    continue
                shopping_cart.sort()
                print(shopping_cart)
            case 4:
                print("Buscar producto")
                product = input("Ingresa el nombre del producto a buscar: ").title()
                if product in shopping_cart:
                    print(f"El producto {product} está en el carrito.")
                else:
                    print(f"El producto {product} no está en el carrito.")
            case 5:
                print("Contar productos del carrito")
                print(f"El carrito tiene {len(shopping_cart)} productos.")
            case 6:
                print("Vaciar el carrito")
                shopping_cart.clear()
                print("El carrito está vacío.")
            case 7:
                print("Saliendo del carrito...")
                break
            case _:
                print("Opción inválida")
    except ValueError:
        print("Por favor, ingresa un número válido.")

