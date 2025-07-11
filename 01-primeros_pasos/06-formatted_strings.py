import os
os.system("cls" if os.name == "nt" else "clear")

# F-strings (formatted strings)
name = "Fabián"
last_name = "Ibarra"
age = 24
text5 = f"Hola, mi nombre es {name} {last_name} y tengo {age} años."
print(text5)