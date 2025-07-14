import os
os.system("cls" if os.name == "nt" else "clear")

# Nonlocal: Permite modificar una variable en un ámbito externo a la función
def outer_function():
    """Función externa que define una variable no local."""
    nonlocal_var = "Soy una variable no local"
    
    def inner_function():
        """Función interna que modifica la variable no local."""
        nonlocal nonlocal_var  # Indica que se usará la variable no local
        nonlocal_var = "He cambiado la variable no local"
        print(nonlocal_var)
    
    inner_function()
    print(nonlocal_var)  # Imprime el valor modificado
outer_function()