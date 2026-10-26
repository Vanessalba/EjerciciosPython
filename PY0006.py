inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}
ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
reposiciones = {'CUS002': 10, 'CUS004': 7}


inventario = inventario_inicial.copy()

avisos = []
for v_ventas in ventas:
    if v_ventas not in inventario:                      
        inventario.setdefault(v_ventas, 0)              
        avisos.append("He añadido el codigo" + v_ventas)        
    inventario[v_ventas] = inventario[v_ventas] - 1

for v_ventas,cantidad in reposiciones.items():
    inventario[v_ventas] = inventario.get(v_ventas,0) + cantidad 

print("INFORME")
print("Inventario", len(inventario))
print("Unidades totales:", sum(inventario.values()))


if not avisos:
    print("-")
else:
    for avisos in avisos:
        print(avisos)


for v_stock in list(inventario):
    if inventario[v_stock] <= 0:
        inventario.pop(v_stock)


codigo = input("Introduce un codigo: ").strip()

if codigo:
    print("El codigo es ", inventario.get(codigo, "No existe"))
      
    

del (inventario)