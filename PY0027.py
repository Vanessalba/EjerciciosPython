# PY0027

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")  # discard no da error si no existe
administradores.add("Marcos")    # sigue estando también en usuarios

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "-> es administrador")
    else:
        print(usuario, "-> NO es administrador")
