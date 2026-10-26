# PY0010 (apartado añadido al PY0006)
# Mostrar el inventario SIN los productos con stock 0 o negativo, usando comprensión.

inventario = {"CUS001": 10, "CUS002": 14, "CUS003": 0, "CUS004": -1}

# Se queda con los productos cuyo stock es mayor que 0
inventario_filtrado = {codigo: stock for codigo, stock in inventario.items() if stock > 0}

print("Inventario completo:", inventario)
print("Inventario sin stock 0 o negativo:", inventario_filtrado)
