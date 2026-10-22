#Ejercicio 1: Viaje en taxi
""" 
Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido. 
Los viajes de más de 20 km tienen 10% de descuento. 
Se necesita mostrar el importe del viaje.
"""

#PROBLEMA
#Calcular y mostrar el importe que debe pagar un pasajero por un viaje en taxi según los kilómetros recorridos.

#ENTRADAS
#kilometros: float, kilómetros recorridos, valor mayor o igual a 0.

#SALIDAS
#importe: float, pesos mexicanos, mostrar con dos decimales y el símbolo $ mediante una tabla.

#REGLAS Y SUPUESTOS
#1. El banderazo es de $35.00
#2. El costo por kilómetro recorrido es de $9.00
#3. Si el viaje es mayor a 20 km, se aplica un descuento del 10% sobre el total del viaje.
#4. Si los kilometros recorridos son exactamente 20 km o menos, no se aplica ningún descuento.
#5. El importe inicial se calcula como: 
#   importe_inicial = 35.00 + (kilometros * 9.00)
#6. Cuando corresponda el descuento, el importe final se calcula como:
#   importe_final = importe_inicial - (importe_inicial * 0.10)
#7. El importe final se muestra con dos decimales y el símbolo $.
#8. Se cocnsideran válidos los valores numéricos finitos mayores o iguales a 0. Cualquier otro valor se considera inválido y se debe mostrar un mensaje de error.

#FUNCIONES
# leerKilometros() -> float:
#   Solicita al usuario los kilómetros recorridos y devuelve
#   la cantidad ingresada como un número decimal.
#
# calcularImporte(kilometros: float) -> float:
#   Recibe los kilómetros recorridos y calcula el importe
#   del viaje.
#   Calcula el importe inicial sumando el banderazo de $35.00
#   al costo de $9.00 por cada kilómetro recorrido.
#   Si los kilómetros son mayores a 20, aplica un descuento
#   del 10% al importe inicial.
#   Devuelve el importe final del viaje.
#
# mostrarImporte(importe: float) -> None:
#   Recibe el importe final del viaje y lo muestra en una
#   tabla utilizando tabulate, con dos decimales y el
#   símbolo de pesos.

#ALGORITMO
#1. Solicitar los kilómetros recorridos mediante la función leerKilometros().
#2. Validar que los kilómetros sean un valor numérico finito mayor o igual a 0.
#3. Calcular el importe del viaje mediante la función calcularImporte(kilometros):
#   importe_inicial = 35.00 + (kilometros * 9.00)
#4. Verificar si se aplica el descuento.
#5. Calcular el importe final.
#6. Si kilometros > 20, calcular el importe final con descuento:
#   importe_final = importe_inicial - (importe_inicial * 0.10)
#7. Mostrar el importe final mediante la función mostrarImporte(importe):

#CASOS PRUEBA
#Caso 1: kilometros = 5
#   importe_inicial = 35.00 + (5 * 9.00) = 35.00 + 45.00 = 80.00
#
#Caso 2: kilometros = 20
#   importe_inicial = 35.00 + (20 * 9.00) = 35.00 + 180.00 = 215.00
#   No se aplica descuento, importe_final = 215.00
#
#Caso 3: kilometros = 21
#   importe_inicial = 35.00 + (21 * 9.00) = 35.00 + 189.00 = 224.00
#   Se aplica descuento del 10%: importe_final = 224.00 - (224.00 * 0.10) = 224.00 - 22.40 = 201.60
#   importe_final = 201.60
#
#Caso 4: kilometros = 30
#   importe_inicial = 35.00 + (30 * 9.00) = 35.00 + 270.00 = 305.00
#   Se aplica descuento del 10%: importe_final = 305.00 - (305.00 * 0.10) = 305.00 - 30.50 = 274.50
#   importe_final = 274.50

#RESTRICCIONES
#1. Implementa exactamente el algoritmo propuesto, sin modificarlo.
#2. Utiliza únicamente las funciones del contrato.
#3. No agreges clases ni funciones auxiliares.
#4. No agregues cálculos, descuentos o tarifas adicionales.
#5. No agregues validaciones ni mensajes que no estén
#6. especificados.
#7. La única biblioteca externa permitida es tabulate.
#8. No llames a las funciones desde este archivo.
#9. Las funciones serán llamadas desde menu/menu.py.