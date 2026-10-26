# PY0043

texto = input("Escribe un texto: ")
texto = texto.lower()          # sin diferenciar mayúsculas/minúsculas
texto = texto.replace(" ", "")  # quitamos los espacios en blanco

for i in range(len(texto)):
    letra = texto[i]
    # find() devuelve la primera posición de la letra.
    # Si es igual a i, es la primera vez que aparece (así no repetimos).
    if texto.find(letra) == i:
        print(letra, "->", texto.count(letra))
