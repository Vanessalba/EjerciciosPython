# PY0005

inscritos = {"Ana", "Luis", "Marta", "Pedro"}

# --- Alta de uno en uno con add() ---
while True:
    nombre = input("Nombre del inscrito (escribe 'fin' para terminar): ")
    if nombre == "fin":
        break
    # Rechazamos vacío o con espacios al principio/final
    if nombre == "" or nombre != nombre.strip():
        print("Nombre no válido (vacío o con espacios al principio/final)")
    else:
        inscritos.add(nombre)

# --- Alta por lotes ---
texto = input("Escribe varios nombres separados por comas: ")
# Comprensión: quitamos espacios con strip() y descartamos los vacíos
nuevos = {n.strip() for n in texto.split(",") if n.strip() != ""}
inscritos.update(nuevos)  # une los dos conjuntos

# --- Copia ---
copia = inscritos.copy()

# --- Dar de baja con remove() ---
baja = input("Nombre que quieres dar de baja: ")
try:
    inscritos.remove(baja)
    print("Baja realizada")
except KeyError:
    # Si no existe, remove() da un error (KeyError). Lo controlamos aquí.
    print("Ese nombre no está inscrito")

# --- Consultar con in ---
consulta = input("¿Qué persona quieres comprobar si está inscrita? ")
if consulta in inscritos:
    print(consulta, "está inscrita")
else:
    print(consulta, "NO está inscrita")

# --- Consultar un grupo de personas ---
grupo = {"Ana", "Carlos", "Lucía"}
comunes = inscritos & grupo  # elementos que están en los dos conjuntos
if len(comunes) > 0:
    print("Del grupo están inscritos:", comunes)
else:
    print("Nadie del grupo está inscrito")

# --- Resumen final ---
print("Total de inscritos:", len(inscritos))
print("Lista ordenada:", sorted(inscritos))
print("Copia (sin la baja):", sorted(copia))
