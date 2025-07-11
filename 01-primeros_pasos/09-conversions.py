import os
os.system("cls" if os.name == "nt" else "clear")

value = 100
type_value = type(value)
print(f"El valor es: {value} y su tipo es: {type_value}")

# Conversión de tipos
# Convertir un entero a cadena
value_str = str(value)
print(f"El valor convertido a cadena es: {value_str} y su tipo es: {type(value_str)}")

# Convertir una cadena a entero (solo si es un número válido)
value_int = int(value_str)
print(f"El valor convertido a entero es: {value_int} y su tipo es: {type(value_int)}")