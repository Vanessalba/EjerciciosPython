# PY0019

while True:
    try:
        numero = int(input("Introduce un número entero impar: "))
        if numero % 2 != 0:
            print("Correcto, el", numero, "es impar.")
            break  # salimos del bucle
        else:
            print("Ese número es par. Debes introducir un número impar.")
    except ValueError:
        print("Eso no es un número entero. Debes introducir un número impar.")
