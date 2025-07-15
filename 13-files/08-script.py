import os
os.system("cls" if os.name == "nt" else "clear")

js_code = """
console.log("Hola desde JavaScript generado por Python");
function suma(a, b) {
    return a + b;
}
"""

with open("script.js", "w") as js_file:
    js_file.write(js_code)

with open("script.js", "r") as js_file:
    content = js_file.read()
    print("Contenido del archivo script.js:")
    print(content)