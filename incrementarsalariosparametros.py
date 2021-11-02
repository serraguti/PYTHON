import pyodbc
servidor = "LOCALHOST"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="
+ servidor + "; Database=" + bbdd + ";UID=" + usuario + "; PWD=" + password)
print("Incrementar salario con parámetros")
#Pedimos los datos al usuario para que el programa
#sea dinámico
print("Introduzca OFICIO")
ofi = input()
print("Introduzca un incremento salarial: ")
incremento = int(input())
cursor = conexion.cursor()
sqlupdate = "update emp set salario = salario + ? where oficio=?"
cursor.execute(sqlupdate, (incremento, ofi))
print("Registros modificados: " + str(cursor.rowcount))
cursor.commit()
cursor.close()
#Abrimos de nuevo el cursor
cursor = conexion.cursor()
sqlselect = "select apellido, oficio, salario from emp where oficio=?"
cursor.execute(sqlselect, (ofi))
print("-----------Empleados----------------")
for apellido, oficio, salario in cursor:
    print(apellido + ", " + oficio + ", " + str(salario))
conexion.close()
print("Fin de programa")