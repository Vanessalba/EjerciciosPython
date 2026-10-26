# PY0009

palabras = ["python", "java   ", "javascript", "go", "rust", "", ""]

# a) Palabra (sin espacios) -> longitud
a = {p.strip(): len(p.strip()) for p in palabras}
print("a)", a)

# b) Igual pero sin cadenas vacías
b = {p.strip(): len(p.strip()) for p in palabras if p.strip() != ""}
print("b)", b)

# c) Clave en mayúsculas si mide más de 5, en minúsculas si no
c = {}
for p in palabras:
    limpia = p.strip()
    if limpia != "":
        if len(limpia) > 5:
            c[limpia.upper()] = len(limpia)
        else:
            c[limpia.lower()] = len(limpia)
print("c)", c)

# c) en una sola línea (versión con comprensión)
c2 = {(p.strip().upper() if len(p.strip()) > 5 else p.strip().lower()): len(p.strip())
      for p in palabras if p.strip() != ""}
print("c) con comprensión:", c2)
