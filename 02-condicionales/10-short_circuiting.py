import os
os.system("cls" if os.name == "nt" else "clear")

# Cortocircuito (Short-circuiting)
# Los operadores lógicos devuelven (SOLO UN VALOR) el primer valor que sea True o False, sin evaluar el resto de la expresión.

# or: se ejecuta hasta que encuentra un valor True o devuelve el último valor si no encuentra ninguno True

True or print("Hola Mundo") or print("Hola Mundo 2") # No se ejecuta porque el primer valor es True
print(False or "") # Se ejecuta porque el primer valor es False y el segundo es un string vacío (Falsy)

# and: se ejecuta hasta que encuentra un valor False y si no encuentra, devuelve el último valor

False and print("Hola Mundo") # No se ejecuta porque el primer valor es False
print(True and "Hola Mundo")  # Se ejecuta porque el primer valor es True

# None
# No se ejecuta cuando name es None, lo cual es Falsy

name = "Fabián"
print(name.upper() and name) # Se ejecuta porque name es un valor truthy