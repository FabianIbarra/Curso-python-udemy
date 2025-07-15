import os
os.system("cls" if os.name == "nt" else "clear")

from translate import Translator

with open("message.txt", mode="r") as my_message:
    message_text = my_message.read()
    print(f"Original message: {message_text}")
    print("Translating message to Spanish...")
    translator = Translator(to_lang="es")
    translated_message = translator.translate(message_text)
    print(f"Mensaje traducido: {translated_message}")

    with open("translated_message.txt", mode="w") as translated_file:
        translated_file.write(translated_message)
        print("Mensaje traducido guardado en 'translated_message.txt'.")