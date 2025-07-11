import os
os.system("cls" if os.name == "nt" else "clear")
# Tipos de datos
# String
nombre = "Fabián"
apellido = "Ibarra"

# Integer
edad = 24

# Float
dinero = 20.50

# Boolean
es_estudiante = True
es_profesor = False

# Datos especiales
# Lista
lenguajes = ["Python", "JavaScript", "Java"]
numeros = [n for n in range(1, 101) if n % 5 == 0]
print(numeros)

# Tupla
meses = ("Enero", "Febrero", "Marzo")

# Set (conjunto)
lenguajes_set = {"Python", "JavaScript", "Java"}

# Diccionario
persona = {
    "nombre": "Fabián",
    "apellido": "Ibarra",
    "edad": 24,
    "es_estudiante": True,
    "lenguajes": ["Python", "JavaScript", "Java"],
    "meses": ("Enero", "Febrero", "Marzo"),
    "lenguajes_set": {"Python", "JavaScript", "Java"}
}

print(persona["nombre"])
print(type(nombre))  # <class 'str'>
print(edad)
print(type(edad))    # <class 'int'>
print(dinero)
print(type(dinero))  # <class 'float'>