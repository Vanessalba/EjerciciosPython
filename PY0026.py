# PY0026: Analiza el PY0025. ¿Qué líneas se deben cambiar si se usa set?
# ¿Tendría sentido hacerlo con tuplas?

# ---------- CON SET (conjunto) ----------
# Cambios en el PY0025:
#   1) La lista inicial:
#        paises = ["España", "Argentina", "Perú"]
#      pasa a ser un conjunto:
#        paises = {"España", "Argentina", "Perú"}
#
#   2) Al añadir:
#        paises.append(pais)   ->   paises.add(pais)
#
#   3) Al ordenar (opciones 1 y 2): sorted(paises) sigue valiendo, porque
#      sorted() devuelve una lista ordenada (un set no tiene orden propio).
#
#   4) Al eliminar: paises.remove(pais) sigue valiendo. Da error (KeyError) si
#      no existe, por eso seguimos comprobando antes con "if pais in paises".
#      También se podría usar paises.discard(pais), que no da error.
#
#   5) Comprobar repetidos: un set NO admite elementos repetidos, así que
#      add() ignoraría un país repetido. Aun así dejamos el "if pais in paises"
#      para poder avisar al usuario de que ya estaba.
#
#   6) len(paises) y el límite de 6 países se quedan igual.
#
# Ejemplo mínimo con set:
paises = {"España", "Argentina", "Perú"}
paises.add("Chile")
paises.add("Chile")  # repetido: no se añade otra vez
print(sorted(paises))
paises.discard("Perú")
print(sorted(paises))

# ---------- CON TUPLAS ----------
# No tiene sentido. Una tupla NO se puede modificar (es inmutable), así que no
# podríamos añadir ni eliminar países. Habría que crear una tupla nueva cada
# vez, por ejemplo:
#     paises = paises + ("Chile",)
# Es más incómodo y no aporta nada. Las tuplas sirven para datos fijos.
