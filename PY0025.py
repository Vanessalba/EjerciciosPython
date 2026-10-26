# PY0025

paises = ["España", "Argentina", "Perú"]
ejecuciones = 0
salir = False

while not salir:
    ejecuciones += 1
    try:
        print("MENÚ. Elija una de las siguientes opciones marcando su número:")
        print("1. Imprimir alfabéticamente en orden ascendente")
        print("2. Imprimir alfabéticamente en orden descendente")
        print("3. Añadir País")
        print("4. Eliminar Pais")
        print("5. Salir")

        opcion = int(input("Opción: "))  # si no es entero, salta ValueError

        if opcion < 1 or opcion > 5:
            print("La opción debe estar entre 1 y 5")
        elif opcion == 1:
            print(sorted(paises))
            print("\n")
        elif opcion == 2:
            print(sorted(paises, reverse=True))
            print("\n")
        elif opcion == 3:
            if len(paises) >= 6:
                print("La lista está llena (máximo 6 países)")
            else:
                pais = input("País a añadir: ").strip().capitalize()
                if pais == "":
                    print("No se puede añadir un país vacío")
                elif pais in paises:
                    print("Ese país ya está en la lista")
                else:
                    paises.append(pais)
                    print("País añadido")
                    print(paises)
                    print("\n")
        elif opcion == 4:
            pais = input("País a eliminar: ").strip().capitalize()
            if pais in paises:
                paises.remove(pais)
                print("País eliminado")
                print(paises)
                print("\n")
            else:
                print("Ese país no está en la lista")
        else:
            salir = True

    except ValueError:
        print("Error: debes escribir un número entero")
    else:
        # Solo se ejecuta si NO hubo error
        if not salir:
            print("#" * 70, end="\n\n")
    finally:
        # Se ejecuta SIEMPRE (haya error o no)
        print("Ejecuciones del menú:", ejecuciones)

print("Gracias por usar el programa.")
print("Número total de intentos:", ejecuciones)
print("¡Hasta pronto!")
