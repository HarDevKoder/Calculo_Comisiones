""" CALCULO DE LAS COMISIONES DE UN EMPLEADO
Se requiere un Algoritmo que solicite 
  - Nombre del empleado
  - Ventas
Calcule
  - Valor en pesos de la comision por ventas —>13%
Imprima en pantalla
  - Nombre del vendedor
  - Valor de las ventas
  - valor de la comision
  - Neto a recibir por el empleado
"""
nombre = input('Ingresa Nombre del Empleado: ')
ventas = round(int(input('Ingresa Ventas Totales: $')))
comision = round(ventas*0.13)
neto = ventas+comision
print("")
print(f"Nombre: {nombre}")
print(f"Ventas: ${ventas:,}")
print(f"Comision (13%): ${comision:,}")
print(f"Neto a pagar: ${neto:,}")
