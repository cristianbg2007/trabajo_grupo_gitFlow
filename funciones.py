# aqui van las funcionesgit checkout develop
#aqui se hizo la funcion de imc
def calcular_imc(peso:float, altura:float):
    imc = peso/altura**2
    return imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: int)-> float:
        imc = calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
        print ("el porcentaje de grasa corporal es:" , imc)
        return imc

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
