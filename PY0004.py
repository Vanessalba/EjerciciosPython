# PY0004

menu_base = ["Ensalada", "Sopa", "Pasta"]

menu_hoy = menu_base.copy()          # copia independiente
menu_hoy.extend(["Pescado", "Postre"])
print("Con especiales:", menu_hoy)

menu_hoy.pop()                       # quita el último plato (Postre)
print("Sin el último:", menu_hoy)

if "Sopa" in menu_hoy:
    menu_hoy.remove("Sopa")
print("Sin la sopa:", menu_hoy)

# Escoger una posición y eliminarla
try:
    posicion = int(input("Posición que quieres eliminar (empieza en 0): "))
    menu_hoy.pop(posicion)
except ValueError:
    print("Tienes que escribir un número")
except IndexError:
    print("Esa posición no existe")
print("Tras eliminar la posición:", menu_hoy)

print("Menú al revés:", menu_hoy[::-1])

menu_base.clear()  # vaciamos la original
print("Menú base:", menu_base)
print("Menú de hoy (no cambia):", menu_hoy)
