# PY0003

# Parte A
asistentes = []
while True:
    nombre = input("Nombre del asistente (escribe 'fin' para terminar): ")
    if nombre == "fin":
        break
    asistentes.append(nombre)

# Parte B
buscado = input("¿Qué nombre quieres consultar? ")
veces = asistentes.count(buscado)
print(f'count("{buscado}")={veces}')

# Parte C
if buscado in asistentes:
    posicion = asistentes.index(buscado)
    print(f'index("{buscado}")={posicion}')
    asistentes.remove(buscado)  # elimina la primera aparición
    print("Tras remove:", asistentes)
else:
    print("Ese nombre no está en la lista")

# Parte D
vip = input("Nombre del asistente VIP: ")
asistentes.insert(0, vip)
print("Lista final:", asistentes)
