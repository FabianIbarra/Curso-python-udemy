import os
os.system("cls" if os.name == "nt" else "clear")

# Introspección de objetos: Obtener información sobre las propiedades y métodos de un objeto
x = [1, 2, 3]
print(type(x))  # Tipo del objeto
print(dir(x))   # Métodos y atributos del objeto
print(x.__doc__)  # Documentación del objeto
print(hasattr(x, '__len__'))  # Verifica si el objeto tiene un atributo o método específico
print(getattr(x, 'append'))  # Obtiene el método 'append' del objeto
print(callable(x.append))  # Verifica si el método 'append' es callable
print(id(x))  # Identificador único del objeto en memoria