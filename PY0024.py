# PY0024

# PY0013 pero con un diccionario para contar las ocurrencias
import time

texto = input("Escribe un texto: ")
viejo = input("Carácter que quieres sustituir: ")
nuevo = input("Carácter nuevo: ")

print("\tCaracteres recibidos")

if len(viejo) != 1 or len(nuevo) != 1:
    print("Debes escribir solo un carácter.")
    time.sleep(3)
    exit()

ocurrencias = {}
for letra in texto:
    ocurrencias[letra] = ocurrencias.get(letra, 0) + 1

print("Ocurrencias de cada carácter:", ocurrencias)

if viejo in ocurrencias:
    print(f"'{viejo}' aparece {ocurrencias[viejo]} veces")
    print("Resultado:", texto.replace(viejo, nuevo))
else:
    print("Ese carácter no aparece en el texto")
