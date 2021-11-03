from conexiondepartamentosmarta import ConexionDepartamentosMarta

print("DEPARTAMENTOS SQL CON CLASES")
#creamos el obeto conexion con el que trabajar
connection= ConexionDepartamentosMarta()
#Todo este código, deseo que se repita hasta que el usuario escriba 4: Necesitamos opción primero para que entre en el bucle
opcion = -1
while (opcion != 4):
    print("1.- Nuevo departamento")
    print("2.- Eliminar departamento")
    print("3.- Modificar departamento")
    print("4.- Salir")
    print("Seleccione una opción:")
    opcion = int(input())
    if (opcion == 1):
        #Llamamos a nuevo dept
        print("-----Insertando-----")
        print ("Introduzca nuevo número de departamento")
        numero= int(input())
        print("Introduzca nuevo nombre")
        nombre=input()
        print("Introduzca nueva localidad")
        localidad=input()
        respuesta= connection.insertarDepartamento (numero, nombre, localidad)
        print("Departamentos insertados: " + str(respuesta))
    elif (opcion == 2):
        #Llamamos a eliminar
        print("-----Eliminando------")
        print("Introduzca un número de departamento para eliminar")
        numero= int(input())
        respuesta=connection.eliminarDepartamento(numero)
        print("Departamentos eliminados: " + str(respuesta))
    elif (opcion == 3):
        #Llamamos a modificar
        print("-----Update------")
        print ("Introduzca número de departamento")
        numero=int(input())
        print("Introduzca nuevo nombre")
        nombre=input()
        print("Introduzca nueva localidad")
        localidad=input()
        respuesta=connection.modificarDepartamento(numero, nombre, localidad)
        print("Departamentos modificados: " + str(respuesta))
    elif (opcion == 4):
        print("Hasta luego")
    else:
        print("Opción incorrecta")
print("Fin de programa")