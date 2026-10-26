# PY0012

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Todas las combinaciones (x, y) cuya suma sea par
combinaciones = [(x, y) for x in lista1 for y in lista2 if (x + y) % 2 == 0]
print(combinaciones)
