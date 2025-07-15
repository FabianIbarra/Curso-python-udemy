import os
os.system("cls" if os.name == "nt" else "clear")

from rich.console import Console # type: ignore
from rich.text import Text # type: ignore
import time

console = Console()

mensaje = "Hola, Python con Rich!"

for letra in mensaje:
    console.print(Text(letra, style="bold magenta"), end="")
    time.sleep(0.1)  # Pausa para simular un efecto de escritura