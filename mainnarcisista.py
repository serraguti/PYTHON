import metodosnarcisista

print("Ejemplo narcisista y bisiesto")
metodosnarcisista.menuNarcisista();
opcion = int(input())
if (opcion == 1):
    print("Introduzca un número")
    numero = int(input())
    metodosnarcisista.isBisiesto(numero)
elif (opcion == 2):
    print("Introduzca un número")
    textonumero = input()
    metodosnarcisista.isNarcisista(textonumero)
else:
    print("Hasta luego")
print("Fin de programa")