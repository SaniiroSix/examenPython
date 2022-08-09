
while(True):
 Opcion = input("""\n¿Qué quieres hacer? Ingresa una opción
    (1) Area de un rectangulo
    (2) Salir"""
    if Opcion == '1' :
          X = float(input("Ingresa el base: \n"))
          Y = float(input("Ingresa el altura: \n"))
          print(f"\n “El área del rectángulo, resultado de multiplicar su base {X} por su altura {Y} es:”".format(X*Y))
    elif Opcion == '2' :
         print("\n Gracias, hasta luego")
        break
    else:
        print ("\n No hay manera. Intenta de nuevo ")
    )
 


