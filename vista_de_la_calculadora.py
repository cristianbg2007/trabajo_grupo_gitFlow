import Calcular_calorías_para_adelgazar as calc


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
            print("Aquí se calculan las calorías por actividad")

        elif opcion == "4":

            print("CALCULADORA DE CALORÍAS PARA ADELGAZAR")

            peso = float(input("Ingrese su peso kg: "))
            altura = float(input("Ingrese su altura en cm: "))
            edad = int(input("Ingrese su edad: "))
            valor_genero = float(
                input("Ingrese 5 para hombre o -161 para mujer: ")
            )

            resultado = calc.consumo_calorias_recomendado_para_adelgazar(
                peso,
                altura,
                edad,
                valor_genero
            )

            print(resultado)

        elif opcion == "5":
            print("Aquí se calculan las calorías en reposo")

        elif opcion == "6":
            print("Usted ha salido del programa")
            break

        else:
            print("Opción inválida")


# Iniciar programa
iniciar_programa()