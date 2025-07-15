import os
os.system("cls" if os.name == "nt" else "clear")

from cowpy import cow

vaca = cow.Cowacter()
print(vaca.milk("Python es genial"))
