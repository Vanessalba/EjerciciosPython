# PY0011

# a) Aplanar una lista de listas
lista = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
plana = [n for sublista in lista for n in sublista]
print("a)", plana)

# b) Solo los pares
pares = [n for sublista in lista for n in sublista if n % 2 == 0]
print("b)", pares)

# c) Traspuesta de una matriz
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
traspuesta = [[fila[i] for fila in matriz] for i in range(len(matriz))]
print("c)", traspuesta)
