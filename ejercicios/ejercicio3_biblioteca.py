#Ejercicio 3: Multa de biblioteca
"""Una biblioteca cobra $5 por cada día de retraso en la devolución de un libro. 
   A partir del día 11 de retraso, cada día cuesta $10.
   La multa máxima es de $200. Se necesita mostrar la multa a partir
   de los días de retraso.
"""

#PROBLEMA
#Calcular y mostrar la multa que debe pagar una personas según los días de retraso en la devolución de un libro.

#ENTRADAS
#dias: int, cantidad de días de retraso, número entero mator o igual a 0.

#SALIDAS
#multa: float, importe de la multa en pesos mexicanos, mostrar con dos decimales.
#El resultado se muestra en una tabla utilizando tabulate.

#REGLAS Y SUPUESTOS
#1. Cada uno de los primeros  días de retraso cuesta $5.00
#2. Apartir del día 11, cada día adicional cuesta $10.00
#3. Si no hay días de retraso, la multa es $0.
#4. Para calcular la multa de más de 10 días, se suman $50.00 correspondientes a los primeros 10 días y $10.00 por cada día adicional.
#5. La multa máxima permitida es de $200.00
#6. Si el cálculo supera $200.00, la multa final será de $200.00
#7. Los días de retraso se consideran números enteros mayor o iguales a 0.
#8. El resultado se muestra con dos decimales.

#CONTRATO DE FUNCIONES
# leerDias() -> int:
#   Solicita al usuario los días de retraso y devuelve la cantidad ingresada como un número entero.
#
# calcularMulta(dias: int) -> float:
#   Recibe los días de retraso y calcula la multa
#   Si dias <= 10, multiplica los días por $5.00
#   Si dias > 10, suma $50 por los primeros 10 días y $10 por cada día adicional
#   Si la multa calculada supera $200, devuelve $200.00
#   Devuelve el importe final de la multa
#
# mostrarMulta(multa: float) -> None:
#   Recibe el importe final de la multa y lo muestra en una tabla utilizando tabulate, con dos decimales y el símbolo de pesos

#ALGORITMO
# 1. Solicitar los días de retraso mediante leerDias().
#
# 2. Calcular la multa mediante calcularMulta(dias):
#       Si dias <= 10:
#           multa = dias * 5
#       En caso contrario:
#           multa = (10 * 5) + ((dias - 10) * 10)
#
# 3. Si la multa calculada supera los $200:
#       multa = 200
#
# 4. Devolver la multa final calculada.
#
# 5. Mostrar la multa mediante mostrarMulta(multa).

#CASOS DE PRUEBA
# 1. dias = 0
#    multa = 0 * 5 = $0.00
#
# 2. dias = 10
#    multa = 10 * 5 = $50.00
#
# 3. dias = 11
#    multa = 50 + ((11 - 10) * 10)
#    multa = 50 + 10 = $60.00
#
# 4. dias = 25
#    multa = 50 + ((25 - 10) * 10)
#    multa = 50 + 150 = $200.00
#
# 5. dias = 40
#    multa = 50 + ((40 - 10) * 10)
#    multa = 50 + 300 = $350.00
#    Como supera $200, la multa final es $200.00

#RESTRICCIONES
#1. Implementa exactamente el algoritmo descrito.
#2. Utiliza únicamente las funciones especificadas en el contrato
#3. No agregues clases ni funciones auxiliares.
#4. No agregues tarifas, descuentos ni reglas adicionales.
#5. No agregues validaciones ni mensajes que no estén especificados
#6. La única biblioteca externa permitida es tabulate
#7. No cambies los límites de las condiciones ni la multa máxima
#8. No llames a las funciones desde este archivo; se llaman desde menu/menu.py

from tabulate import tabulate


def leerDias() -> int:
    return int(input("Ingrese los días de retraso: "))


def calcularMulta(dias: int) -> float:
    if dias <= 10:
        multa = dias * 5
    else:
        multa = (10 * 5) + ((dias - 10) * 10)

    if multa > 200:
        multa = 200

    return float(multa)


def mostrarMulta(multa: float) -> None:
    tabla = [["Multa final", f"${multa:.2f}"]]
    print(tabulate(tabla, headers=["Concepto", "Importe"], tablefmt="grid"))