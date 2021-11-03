import pyodbc
servidor="LOCALHOST"
bbdd="HOSPITAL"
usuario="sa"
password="azure"
conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=" + servidor
+ "; Database=" + bbdd + ";UID=" + usuario + "; PWD=" + password)
cursor = conexion.cursor()
sqlselect = "select inscripcion, apellido from enfermo"
cursor.execute(sqlselect)
print("-----Listado de enfermos-------")
for ins, ape in cursor:
    print(str(ins) + " - " + ape)
cursor.close()
print("Escriba una inscripción de enfermo para eliminar")
inscripcion = int(input())
sqldelete = "delete from enfermo where inscripcion=?"
cursor = conexion.cursor()
cursor.execute(sqldelete, (inscripcion))
print("Registros eliminados: " + str(cursor.rowcount))
cursor.commit()
cursor.close()
conexion.close()
print("Fin de programa")
