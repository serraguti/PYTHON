import pyodbc
servidor = "LOCALHOST"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="
+ servidor + "; Database=" + bbdd + ";UID=" + usuario + "; PWD=" + password)
#Pedimos los datos al usuario para que el programa
#sea dinámico
print("Introduzca OFICIO")
ofi = input()
print("Introduzca un incremento salarial: ")
incremento = input()
cursor = conexion.cursor()
#sqlupdate = "update emp set salario = salario + 1 where oficio='DIRECTOR'"
sqlupdate = "update emp set salario = salario + " + incremento + " where oficio='" + ofi + "'"
cursor.execute(sqlupdate)
print("Registros modificados: " + str(cursor.rowcount))
cursor.commit()
cursor.close()
#Abrimos de nuevo el cursor
cursor = conexion.cursor()
#sqlselect = "select apellido, oficio, salario from emp where oficio='DIRECTOR'"
sqlselect = "select apellido, oficio, salario from emp where oficio='" + ofi + "'"
cursor.execute(sqlselect)
print("-----------Empleados----------------")
for apellido, oficio, salario in cursor:
    print(apellido + ", " + oficio + ", " + str(salario))
conexion.close()
print("Fin de programa")