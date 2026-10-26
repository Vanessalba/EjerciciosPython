# PY0023

# PY0013 pero usando set
import time

texto = input("Escribe un texto: ")
viejo = input("Carácter que quieres sustituir: ")
nuevo = input("Carácter nuevo: ")

print("\tCaracteres recibidos")

if len(viejo) != 1 or len(nuevo) != 1:
    print("Error: debes escribir solo un carácter.")
    time.sleep(3)
    exit()

letras_distintas = set(texto)  # set con los caracteres sin repetir

if viejo in letras_distintas:
    print("Resultado:", texto.replace(viejo, nuevo))
else:
    print("Ese carácter no aparece en el texto")
print("Caracteres distintos del texto:", len(letras_distintas))
