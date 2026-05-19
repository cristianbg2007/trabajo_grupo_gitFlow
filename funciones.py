# aqui van las funciones

#calcular calorias en actividad
def calcular_calorias_actividad() -> None:
    print("\n--- CALORÍAS POR ACTIVIDAD ---")

    peso = float(input("Ingrese su peso en kg: "))
    minutos = int(input("Ingrese la cantidad de minutos: "))

    print("\nActividades disponibles:")
    print("1. Caminar")
    print("2. Correr")
    print("3. Bicicleta")

    actividad = input("Seleccione una actividad: ")

    # Calorías quemadas por minuto aproximadas
    if actividad == "1":
        calorias = minutos * (3.5 * peso / 200)
        nombre = "caminar"

    elif actividad == "2":
        calorias = minutos * (7 * peso / 200)
        nombre = "correr"

    elif actividad == "3":
        calorias = minutos * (6 * peso / 200)
        nombre = "bicicleta"

    else:
        print("Actividad inválida")
        return

    print(f"\nUsted quemó aproximadamente {calorias:.2f} calorías al {nombre}.")