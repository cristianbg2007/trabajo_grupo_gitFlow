import funciones 
def mostrar_menu()-> str :
    print("1. Calcular el imc")
    print("2. Calcular porcentaje de grasa")
    print("3. calcular calorias actividad ")
    print("4. calcular calorias para adelgazar ")
    print("5. calcular calorias en reposo ")
    print("6. Salir")
    opcion= input("ingrese la opcion que desea ejecutar: ")
    return opcion



            
def iniciar_programa()-> None:
   opcion= mostrar_menu()
   if opcion =="1":
       peso= float(input("ingrese el peso en kilogramos:"))
       altura= float(input("ingrese la altura en metros:"))
       funciones.calcular_imc(peso, altura)
       print("el indice de masa corporal es de : ", funciones.calcular_imc(peso, altura))
  #  elif opcion =="2":
        #aqui se ejecuta porcentaje de grasa()
   # elif opcion =="3":
        #aqui se ejecuta calcular calorias actividad()
    #  elif opcion =="4":
        #aqui se ejecuta calorias para adelgazar()
     # elif opcion =="5":
        #aqui se ejecuta calorias en reposo()
      #else: 
   # print("usted ha salido del programa")

iniciar_programa()