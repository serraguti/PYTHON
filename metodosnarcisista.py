def menuNarcisista():
    print("-------------Menu--------------")
    print("0.- Salir")
    print("1.- Año Bisiesto")
    print("2.- Número narcisista")
    print("Seleccione una opción: ")

def isBisiesto(anyo):
   if (anyo%4 == 0):
       if (anyo%100 != 0 or anyo%400 == 0):
           print("BISIESTO")
       else:
           print("no es bisiesto")
   else:
       print("No es bisiesto")

def isNarcisista(textonumero):
    suma = 0
    longitud = len(textonumero)
    for i in range(longitud):
        caracter = textonumero[i]
        numero = int(caracter)
        #potencia = numero**longitud
        potencia = pow(numero, longitud)
        suma = suma + potencia
    
    if (suma == int(textonumero)):
        print("Narcisista!!!")
    else:
        print("No es narcisista")
