# PY0020

while True:
    print()
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("Escribe 'salir' para terminar")

    # strip() quita espacios y lower() pasa a minúsculas
    opcion = input("Elige una opción: ").strip().lower()

    if opcion == "salir":
        print("Adiós")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida")
        continue  # vuelve a mostrar el menú

    try:
        n1 = int(input("Primer número entero: "))
        n2 = int(input("Segundo número entero: "))
    except ValueError:
        print("Error: tienes que escribir números enteros")
        continue

    if opcion == "1":
        resultado = n1 + n2
    elif opcion == "2":
        resultado = n1 - n2
    elif opcion == "3":
        resultado = n1 * n2
    else:
        if n2 == 0:
            print("Error: no se puede dividir entre cero")
            continue
        resultado = n1 / n2

    print(f"Resultado: {resultado:.2f}")
