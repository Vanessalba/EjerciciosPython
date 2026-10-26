# PY0002

precios = [1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4]

for i in range(len(precios)):
    antes = precios[i]

    if antes < 0:
        continue  # precio negativo: saltamos este elemento

    if i % 2 == 0:
        despues = antes * 0.90  # índice par: 10% de descuento
    else:
        despues = antes * 0.80  # índice impar: 20% de descuento

    precios[i] = despues  # actualizamos la lista original
    print(f"indice_lista={i}, precio_antes={antes:.2f}, precio_después={despues:.2f}")

print("Lista final:", precios)
