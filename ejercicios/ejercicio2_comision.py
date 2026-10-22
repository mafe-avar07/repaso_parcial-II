#Ejercicio 2: Cálculo de comisión
"""
Un vendedor gana 5% de comisión sobre sus ventas del mes.
Si vende $10,000 o más, la comisión es de 8%.
Si vende más de $50,000, recibe además un bono de $1,000.
Se necesita mostrar la comisión, el bono y el total a pagar.
"""

#PROBLEMA
#Calcular y mostrar la comisión, el bono y el total a pagar a un vendedor según sus ventas del mes.

#ENTRADAS
#ventas: float, ventas del mes en pesos mexicanos, valor mayor o igual a 0.

#SALIDAS
#comision: float, comisión en pesos mexicanos, mostrar con dos decimales y el símbolo $.
#bono: float, bono en pesos mexicanos, mostrar con dos decimales y el símbolo $ mediante una tabla.
#total: float, total a pagar en pesos mexicanos, mostrar con dos decimales y el símbolo $.
#Los resultados se mostrarán en una tabla utilizando tabulate.

#REGLAS Y SUPUESTOS
#1. Si las ventas son menores a $10,000, la comisión es del 5%.
#2. Si las ventas son iguales o mayores a $10,000, la comisiónes del 8%.
#3. Si las ventas son mayores a $50,000, se otorga un bono de $1,000.
#4. Si las ventas son iguales o menores a $50,000, el bono es $0.
#5. La comisión se calcula sobre el total de las ventas mensuales.
#6. La comisión se calcula multiplicando las ventas por el porcentaje correspondiente.
#7. El bono se suma a la comisión para obtener el total a pagar.
#8. El total a pagar incluye únicamente la comisión y el bono; no se considera un sueldo base porque el enunciado no lo indica.
#9. Los importes se muestran con dos decimales.
#10. Las ventas válidas son cantidades numéricas mayores o igualesa 0. 

#CONTRATO DE FUNCIONES
#leerVentas() -> float:
#   Solicita al usuario las ventas del mes y devuelve
#   la cantidad ingresada como un número decimal.
#
#calcularComision(ventas: float) -> float:
#   Recibe las ventas del mes y calcula la comisión colculanda.
#   Si ventas < 10000, la comisión es del 5%.
#   Si ventas >= 10000, la comisión es del 8%.
#
#calcularBono(ventas: float) -> float:
#   Recibe las ventas del mes y calcula el bono correspondiente.
#   Si ventas > 50000, el bono es de $1,000; en caso contrario, es de $0.
#
#mostrarPago(comision: float, bono: float, total: float) -> None:
#   Recibe la comisión, el bono y el total a pagar y los muestra en una tabla con tabulate utilizando dos decimales y el símbolo $.

#ALGORITMO
#1. Solicitar las ventas del mes mediante la función leerVentas().
#2. Calcular la comisión mediante la función calcularComision(ventas):
#   Si ventas < 10000:
#       comision = ventas * 0.05
#   En caso contrario:
#       comision = ventas * 0.08
#3. Calcular el bono mediante la función calcularBono(ventas):
#   Si ventas > 50000:
#       bono = 1000
#   En caso contrario:
#       bono = 0
#4. Calcular el total a pagar sumando la comisión y el bono:
#   total = comision + bono
#5. Mostrar la comisión, el bono y el total a pagar mediante la función mostrarPago(comision, bono, total).

#CASOS PRUEBA
#Caso 1: ventas = 5000
#   comision = 5000 * 0.05 = 250.00
#   bono = 0
#   total = 250.00 + 0 = $250.00
#
#Caso 2: ventas = 10000
#   comision = 10000 * 0.08 = 800.00
#   bono = 0
#   total = 800.00 + 0 = $800.00
#
#Caso 3: ventas = 50000
#   comision = 50000 * 0.08 = 4000.00
#   bono = 0
#   total = 4000.00 + 0 = $4000.00
#
#Caso 4: ventas = 50001
#   comision = 50001 * 0.08 = 4000.08
#   bono = 1000
#   total = 4000.08 + 1000 = $5000.08
#
#RESTRICCIONES
#1. Implementa exactamente el algoritmo descrito.
#2. Utiliza únicamente las funciones especificadas en el contrato.
#3. No agregues clases ni funciones auxiliares.
#4. No agregues sueldos base, incentivos ni cálculos adicionales.
#5. No agregues validaciones ni mensajes que no estén especificados.
#6. La única biblioteca externa permitida es tabulate.
#7. No cambies los porcentajes ni los límites de las condiciones.
#8. No llames a las funciones desde este archivo; se llaman desde menu/menu.py.