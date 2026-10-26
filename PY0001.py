# PY0001

tareas = ["Limpiar", "Comprar Comida", "Salir"]

# enumerate(lista, 1) da el número (empezando en 1) y el elemento
for numero, tarea in enumerate(tareas, 1):
    print(f"{numero}. {tarea}")
