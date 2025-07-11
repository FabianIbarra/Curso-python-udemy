import os
os.system("cls" if os.name == "nt" else "clear")

print("\tFunciones incorporadas(nativas) en Python\n")
# Funciones incorporadas
# Estas funciones están disponibles en Python sin necesidad de importarlas
# y se pueden utilizar directamente en el código.
# Algunas de las funciones incorporadas más comunes son:
# - print(): Imprime un mensaje en la consola.
# - len(): Devuelve la longitud de un objeto (como una cadena, lista, etc
# - type(): Devuelve el tipo de un objeto.
# - int(), float(), str(): Funciones de conversión de tipos de datos.
# - input(): Permite al usuario ingresar datos desde la consola.
# - range(): Genera una secuencia de números enteros.
# - sum(): Suma los elementos de un iterable (como una lista).
# - max(), min(): Devuelven el valor máximo o mínimo de un iterable.
# - sorted(): Ordena los elementos de un iterable.
# - abs(): Devuelve el valor absoluto de un número.
# - round(): Redondea un número a un número específico de decimales.
# - all(), any(): Devuelven True si todos o al menos uno de los elementos
#   de un iterable son verdaderos, respectivamente.
# - zip(): Combina varios iterables en un solo iterable de tuplas.
# - map(): Aplica una función a cada elemento de un iterable.
# - filter(): Filtra los elementos de un iterable según una función.
# - enumerate(): Devuelve un iterable que contiene pares de índice y valor
#   de un iterable.
# - dir(): Devuelve una lista de los atributos y métodos de un objeto.
# - help(): Muestra la documentación de un objeto o función.
# - id(): Devuelve el identificador único de un objeto en memoria.
# - isinstance(): Verifica si un objeto es una instancia de una clase o tipo específico.
# - eval(): Evalúa una expresión de Python y devuelve su resultado.
# - exec(): Ejecuta un bloque de código Python dinámicamente.
# - globals(), locals(): Devuelven los diccionarios de variables globales
#   y locales, respectivamente.
# - format(): Formatea una cadena de texto según un formato específico.
# - chr(), ord(): Convierte un número entero a su carácter ASCII y viceversa.
# - reversed(): Devuelve un iterable con los elementos en orden inverso.
# - slice(): Crea un objeto de corte para acceder a una parte de un iterable.
# - memoryview(): Crea una vista de memoria de un objeto de bytes.
# - isinstance(): Verifica si un objeto es una instancia de una clase o tipo específico.
# - callable(): Verifica si un objeto es llamable (es decir, si se puede llamar como una función).
# - next(): Devuelve el siguiente elemento de un iterador.
# - iter(): Devuelve un iterador para un objeto iterable.

# Métodos
# Los métodos son funciones que están asociadas a un objeto y se utilizan
# para realizar operaciones específicas en ese objeto. Los métodos se
# invocan utilizando la notación de punto (objeto.método()).

message = "Es un buen programador"
new_message = message.replace("Es", "Soy")
print(new_message)