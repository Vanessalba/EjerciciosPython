# PY0007

import copy

# Datos de ejemplo (el enunciado no los incluía, he puesto estos)
calificaciones = [
    {"alumno": "Ana", "modulo": "Programación", "nota": 7.5},
    {"alumno": "Ana", "modulo": "Sistemas", "nota": 8.0},
    {"alumno": "Luis", "modulo": "Sistemas", "nota": 6.0},
    {"alumno": "Marta", "modulo": "Programación", "nota": 9.0},
    {"alumno": "Ana", "modulo": "Programación", "nota": 4.0},
    {"alumno": "Luis", "modulo": "Programación", "nota": 3.5},
]

# 1. Estructura anidada: {alumno: {modulo: [notas]}}
alumnos = {}
for c in calificaciones:
    alumnos.setdefault(c["alumno"], {}).setdefault(c["modulo"], []).append(c["nota"])
print("Alumnos:", alumnos)

# 2. Media de las notas máximas de cada módulo por alumno
medias = {}
for alumno, modulos in alumnos.items():
    maximas = []
    for modulo, notas in modulos.items():
        if len(notas) > 0:  # si no tiene nota, no cuenta
            maximas.append(max(notas))
    if len(maximas) > 0:
        medias[alumno] = sum(maximas) / len(maximas)
print("Medias:", medias)

# 3. Por módulo, cada alumno con su nota máxima
maximos_modulo = {}
for alumno, modulos in alumnos.items():
    for modulo, notas in modulos.items():
        maximos_modulo.setdefault(modulo, {})[alumno] = max(notas)
print("Máximas por módulo:", maximos_modulo)

# 4. Aprobados (nota media del módulo >= 5) con comprensión de diccionarios
aprobados = {
    alumno: {m: sum(n) / len(n) for m, n in modulos.items() if sum(n) / len(n) >= 5}
    for alumno, modulos in alumnos.items()
}
print("Aprobados:", aprobados)

# 5. Correcciones sobre la última nota (trabajamos con una copia profunda)
correcciones = {"Ana": {"Programación": +0.75}}
alumnos2 = copy.deepcopy(alumnos)
for alumno, modulos in correcciones.items():
    for modulo, cambio in modulos.items():
        if alumno in alumnos2 and modulo in alumnos2[alumno]:
            alumnos2[alumno][modulo][-1] += cambio
print("Tras correcciones:", alumnos2)

# 6. Eliminar una nota concreta
def eliminar_nota(datos, alumno, modulo, indice):
    nota = datos[alumno][modulo].pop(indice)
    if len(datos[alumno][modulo]) == 0:
        datos[alumno].pop(modulo)      # módulo sin notas: lo quitamos
    if len(datos[alumno]) == 0:
        datos.pop(alumno)              # alumno sin módulos: lo quitamos
    return nota

borrada = eliminar_nota(alumnos2, "Ana", "Programación", 0)
print("Nota eliminada:", borrada)
print("Resultado:", alumnos2)
