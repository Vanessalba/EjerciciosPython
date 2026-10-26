# PY0013

import time

texto = input("Escribe un texto: ")
viejo = input("Carácter que quieres sustituir: ")
nuevo = input("Carácter nuevo: ")

print("\tCaracteres recibidos")  # \t es la tabulación

# Comprobamos que sea solo UN carácter en cada caso
if len(viejo) != 1 or len(nuevo) != 1:
    print("Error: debes escribir solo un carácter.")
    time.sleep(3)  # espera 3 segundos
    exit()         # cierra el programa

resultado = texto.replace(viejo, nuevo)
print("Resultado:", resultado)

# ¿Qué se modificaría para cambiar solo las dos primeras ocurrencias?
# Se añade un tercer parámetro a replace():
#     resultado = texto.replace(viejo, nuevo, 2)
