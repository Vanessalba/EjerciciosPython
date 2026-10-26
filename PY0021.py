# PY0021

lista = [10, 15, 100, 40, 35, 353, 400, 40, 500, 420, 340, 115]

# Quitamos el 40 y los mayores de 339, y ordenamos de menor a mayor
resultado = sorted([n for n in lista if n != 40 and n <= 339])
print(resultado)
