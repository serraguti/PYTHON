import metodosnarcisista

print("Ejemplo narcisista y bisiesto")
opcion = -1
while (opcion != 0):
    metodosnarcisista.menuNarcisista();
    opcion = int(input())
    if (opcion == 1):
        print("Introduzca un año")
        numero = int(input())
        respuesta = metodosnarcisista.isBisiesto(numero)
        if (respuesta == True):
            print("AÑO Bisiesto!!!")
        else:
            print("AÑO NO BISIESTO")
    elif (opcion == 2):
        print("Introduzca un número")
        textonumero = input()
        respuesta = metodosnarcisista.isNarcisista(textonumero)
        if (respuesta == True):
            print("NARCISISTA")
        else:
            print("El número NO es narcisista")
    else:
        print("Hasta luego")
print("Fin de programa")