import os
os.system("cls" if os.name == "nt" else "clear")
###
# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales con conocimientos en Python para RH.
# Obtendrás el nombre del candidato, años de experiencia y habilidades.

# Evaluarás:
# * Si el candidato sabe Python/Django, tiene +3 años de experiencia: Candidato Óptimo.
# * Si sabe Python/Django, tiene +1 año de experiencia: Buen candidato.
# * Si sabe Python/Django, tiene 0 años de experiencia: Posible candidato
# * Si no sabe Python: No óptimo, se guardará CV.

# Consejo: Ocupa los métodos .split().
###

# Solicitar datos al usuario
name = input("Ingrese el nombre del candidato: ").title()
while True:
    try:
        experience = int(input("Ingrese los años de experiencia del candidato: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido para los años de experiencia.")
skills = input("Ingrese las habilidades del candidato (separadas por comas): ").title().split(", ")

# Evaluar al candidato
# print(skills)
if "Python" or "Django" in skills and experience >= 3:
    print(f"{name} es un candidato óptimo.")
elif "Python" or "Django" in skills and experience >= 1:
    print(f"{name} es un buen candidato.")
elif "Python" or "Django" in skills and experience <= 0:
    print(f"{name} es un posible candidato.")
else:
    print(f"{name} no es un candidato óptimo, se guardará su CV.")