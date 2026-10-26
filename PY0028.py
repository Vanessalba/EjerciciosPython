# PY0028

nombre_pizzeria = "Pizzería La Beata"

# Cada precio en una variable distinta
precio_margarita = 8.95
precio_pepperoni = 10.50
precio_cuatro_quesos = 11.25
precio_extra_queso = 1.25
precio_extra_champinones = 0.90
precio_extra_jamon = 1.50

terminado = False
while not terminado:
    print("=== " + nombre_pizzeria + " ===")
    try:
        dinero = float(input("¿Cuánto dinero tienes? "))
    except ValueError:
        print("Escribe un número válido")
        continue

    print("Pizzas disponibles:")
    print("1. Margarita", precio_margarita, "$")
    print("2. Pepperoni", precio_pepperoni, "$")
    print("3. Cuatro quesos", precio_cuatro_quesos, "$")
    eleccion = input("Elige una pizza (1-3): ")

    if eleccion == "1":
        nombre_pizza = "Margarita"
        precio_pizza = precio_margarita
    elif eleccion == "2":
        nombre_pizza = "Pepperoni"
        precio_pizza = precio_pepperoni
    elif eleccion == "3":
        nombre_pizza = "Cuatro quesos"
        precio_pizza = precio_cuatro_quesos
    else:
        print("Opción no válida. Empezamos de nuevo.")
        continue

    total = round(precio_pizza, 2)
    print(f"La pizza {nombre_pizza} cuesta {total:.2f}$. Te quedan {dinero - total:.2f}$")

    # Listas para recordar los extras elegidos
    nombres_extras = []
    precios_extras = []

    while True:
        print("Ingredientes extra:")
        print("1. Extra de queso", precio_extra_queso, "$")
        print("2. Extra de champiñones", precio_extra_champinones, "$")
        print("3. Extra de jamón", precio_extra_jamon, "$")
        print("0. No quiero más extras")
        extra = input("Elige un extra: ")

        if extra == "0":
            break
        elif extra == "1":
            nombres_extras.append("Extra de queso")
            precios_extras.append(precio_extra_queso)
            total = round(total + precio_extra_queso, 2)
        elif extra == "2":
            nombres_extras.append("Extra de champiñones")
            precios_extras.append(precio_extra_champinones)
            total = round(total + precio_extra_champinones, 2)
        elif extra == "3":
            nombres_extras.append("Extra de jamón")
            precios_extras.append(precio_extra_jamon)
            total = round(total + precio_extra_jamon, 2)
        else:
            print("Opción no válida")
        print(f"Total: {total:.2f}$. Te quedan {dinero - total:.2f}$")

    if dinero >= total:
        cambio = round(dinero - total, 2)
        # Cambiamos el punto por la coma para que se vea como en el ejemplo
        total_txt = f"{total:.2f}".replace(".", ",")
        cambio_txt = f"{cambio:.2f}".replace(".", ",")
        dinero_txt = f"{dinero:.0f}"

        print("--- Su Pedido ---")
        print(f"El total de su pedido es {total_txt}$")
        print(f"Su cambio de {dinero_txt}$ es: {cambio_txt}$")
        print()
        print(f"-{nombre_pizza} {f'{precio_pizza:.2f}'.replace('.', ',')}$")
        for i in range(len(nombres_extras)):
            precio_txt = f"{precios_extras[i]:.2f}".replace(".", ",")
            print(f"-{nombres_extras[i]} {precio_txt}$")
        print()
        print("Gracias por su visita")
        terminado = True
    else:
        print("No tienes dinero suficiente. Vuelve a empezar.")
