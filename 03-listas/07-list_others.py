import os
os.system("cls" if os.name == "nt" else "clear")

numbers = list(range(1, 101))
print(numbers)

sentence = " ".join(["Hola", "Mundo", "desde", "un", "join"])
print(sentence)

total = sum(numbers)
print(total)

mayor = max(numbers)
print(mayor)

menor = min(numbers)
print(menor)

elementos = len(numbers)
print(elementos)