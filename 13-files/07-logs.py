import os
os.system("cls" if os.name == "nt" else "clear")

from datetime import datetime

message = "Error en servidor"
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("logs.txt", mode="a") as log_file:
    log_file.write(f"[{date}] {message}\n")