# PY0014

# Función pequeña para pedir un número decimal sin que el programa falle
def pedir_numero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Eso no es un número. Inténtalo otra vez.")

n1 = pedir_numero("Primer número: ")
n2 = pedir_numero("Segundo número: ")
n3 = pedir_numero("Tercer número: ")

media = n1 * 0.15 + n2 * 0.35 + n3 * 0.50
print(f"La media ponderada es: {media:.2f}")
