import pyodbc
servidor= "LOCALHOST"
bbdd="HOSPITAL"
usuario="sa"
password="azure"

class ConexionDepartamentosMarta:
    def __init__(self):
        #crear una conexion para trabajar con cualquier metodo de consulta
        self.conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=" + servidor
        + "; Database=" + bbdd + ";UID=" + usuario + "; PWD=" + password)
    #creamos un menu para Main
    def insertarDepartamento (self, numero, nombre, localidad):
        #entrar y salir
        cursor=self.conexion.cursor()
        sqlinsert= "insert into dept values (?, ?, ?)"
        cursor.execute(sqlinsert, (numero, nombre, localidad))
        result=cursor.rowcount
        cursor.commit()
        cursor.close()
        return result

    def eliminarDepartamento (self, numero):
        cursor=self.conexion.cursor()
        sqldelete= "delete from dept where dept_no=?"
        cursor.execute(sqldelete, (numero))
        result=cursor.rowcount
        cursor.commit()
        cursor.close()
        return result

    def modificarDepartamento (self, numero, nombre, localidad):
        cursor=self.conexion.cursor()        
        sqlupdate= "update dept set dnombre=?, loc=? where dept_no=?"
        cursor.execute(sqlupdate, (nombre, localidad, numero))
        result=cursor.rowcount
        cursor.commit()
        cursor.close()
        return result