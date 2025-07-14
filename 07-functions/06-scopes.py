import os
os.system("cls" if os.name == "nt" else "clear")

# Scopes: Ámbitos de visibilidad de las variables (Alcance de las variables)
# Define donde una variable es accesible en el código
global_var = "Soy una variable global"

def local_scope():
    """Función que define una variable local."""
    local_var = "Soy una variable local"
    def inner_scope():
        """Función interna que define una variable local."""
        inner_var = "Soy una variable interna"
        print(global_var)  # Acceso a la variable global
        print(local_var)  # Acceso a la variable local
        print(inner_var)
    inner_scope()

local_scope()