from menu.menu import mostrarMenu
from menu.menu import mostrarMenu, ejecutarEjercicio3

def main():
    while True:
        opcion = mostrarMenu()

        if opcion == "1":
            print("Ejercicio 1 pendeinte.")
        elif opcion == "2":
            print("Ejercicio 2 pendiente.")
        elif opcion == "3":
            ejecutarEjercicio3()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()