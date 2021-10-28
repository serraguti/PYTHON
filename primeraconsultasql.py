import pyodbc
print("Primera consulta SQL Server")
servidor="LOCALHOST"
bbdd="HOSPITAL"
usuario="SA"
password="azure"
#CADENA CONEXION CON SEGURIDAD SQL SERVER (REMOTO)
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
print("Intentando conectar...")
conexion = pyodbc.connect(cadenaconexion)
print("Conectado!!!")
#CURSOR se crea con una conexión abierta
cursor = conexion.cursor()
#Necesitamos una consulta, el cursor 
#maneja tanto consultas de selección (SELECT)
#como consultas de acción, no le importa
#Creamos la consulta select
#No es conveniente utilizar el *
sql = "select dept_no, dnombre, loc from dept"
#El cursor ejecutará la consulta
cursor.execute(sql)
print("Número filas: " + str(cursor.rowcount))
for numero, nombre, localidad in cursor:
    print(str(numero) + ", " + nombre + ", " + localidad)

cursor.close()
conexion.close()
print("Fin de programa")