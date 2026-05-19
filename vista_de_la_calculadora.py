from funciones import calcular_calorias_actividad


def mostrar_menu() -> str:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular el IMC")
    print("2. Calcular porcentaje de grasa")
    print("3. Calcular calorías por actividad")
    print("4. Calcular calorías para adelgazar")
    print("5. Calcular calorías en reposo")
    print("6. Salir")

    opcion = input("Ingrese la opción que desea ejecutar: ")
    return opcion


def iniciar_programa() -> None:

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            print("Aquí se calcula el IMC")

        elif opcion == "2":
            print("Aquí se calcula el porcentaje de grasa")

        elif opcion == "3":
          calcular_calorias_actividad()

        elif opcion == "4":
            print("Aquí se calculan las calorías para adelgazar")

        elif opcion == "5":
            print("Aquí se calculan las calorías en reposo")

        elif opcion == "6":
            print("Usted ha salido del programa")
            break

        else:
            print("Opción inválida")


# Iniciar programa
iniciar_programa()
