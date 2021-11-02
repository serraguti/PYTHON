import pyodbc
servidor = "LOCALHOST"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
print("Introduzca un número")
#El número será un STRING porque lo voy a concatenar abajo
numero = input()
print("Introduzca nombre departamento")
nombre = input()
print("Introduzca localidad")
localidad = input()
#Creamos el cursor
cursor = conexion.cursor()
#sql = "insert into dept values (66, 'PROGRAMACION', 'IBIZA')"
sql = "insert into dept values(" + numero + ", '" + nombre + "', '" + localidad + "')"
print(sql)
#Ejecutamos la consulta
cursor.execute(sql)
#Vamos a imprimir ROWCOUNT para averiguar si tenemos contenido en la
#propiedad
#Rowcount viene con valor en las consultas de acción
#indica el número de filas que han sido afectadas por la consulta
print("Rowcount: " + str(cursor.rowcount))
#Cuando realizamos consultas de acción, todas las acciones
#son temporales, es decir, no se llevan a la bbdd
#Para llevar las consultas de acción a la base de datos de forma
#permanente, debemos realizar un commit sobre el cursor
cursor.commit()
#Cerramos el cursor
cursor.close()
#Vamos a intentar reutilizar el cursor para mostrar
#los departamentos
sqlselect = "select dept_no, dnombre, loc from dept"
#Volvemos a cargar el cursor con la conexion
cursor = conexion.cursor()
#Ejecutamos el cursor cerrado
cursor.execute(sqlselect)
print("------------------Departamentos--------------")
for row in cursor:
    print(row.dnombre + ", " + row.loc)
#Cerramos el cursor
cursor.close()
#Cerramos la conexion
conexion.close()
print("Fin de programa")