def mostrarMenu():
    print("=== Menú Principal ===")
    print("1. Opción 1. Viaje en taxi")
    print("2. Opción 2. Comisión de ventas")
    print("3. Opción 3. Multa de biblioteca")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")
    return opcion


from ejercicios.ejercicio3_biblioteca import (
    leerDias,
    calcularMulta,
    mostrarMulta
)


def ejecutarEjercicio3():
    dias = leerDias()
    multa = calcularMulta(dias)
    mostrarMulta(multa)
