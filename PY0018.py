# PY0018

registro = "zeréP nauJ,01"
registro = registro[::-1]  # [::-1] le da la vuelta -> "10,Juan Pérez"

partes = registro.split(",")  # separa por la coma -> ["10", "Juan Pérez"]
nota = partes[0]
nombre = partes[1]

print(f"{nombre} ha sacado un {nota}.")
