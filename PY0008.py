# PY0008

cuadrados = [n ** 2 for n in range(1, 21)]
print("Cuadrados:", cuadrados)

impares = [n for n in cuadrados if n % 2 != 0]
print("Cuadrados impares:", impares)
