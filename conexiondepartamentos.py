import pyodbc
from departamento import Departamento
servidor="LOCALHOST"
bbdd="HOSPITAL"
usuario="SA"
password="azure"

class ConexionDepartamentos:
    def __init__(self):
        self.conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=" + servidor
        + "; Database=" + bbdd + ";UID=" + usuario + "; PWD=" + password)
    
    def insertarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sqlinsert = "insert into dept values (?,?,?)"
        cursor.execute(sqlinsert, (numero, nombre, localidad))
        result = cursor.rowcount
        cursor.commit()
        cursor.close()
        return result


    def modificarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sqlupdate = "update dept set dnombre=?, loc=? where dept_no=?"
        #sqlupdate = "update dept set dnombre=? where dept_no=?"
        cursor.execute(sqlupdate, (nombre, localidad, numero))
        result = cursor.rowcount
        cursor.commit()
        cursor.close()
        return result

    def eliminarDepartamento(self, numero):
        cursor = self.conexion.cursor()
        sqldelete = "delete from dept where dept_no=?"
        cursor.execute(sqldelete, (numero))
        result = cursor.rowcount
        cursor.commit()
        cursor.close()
        return result

    def buscarDepartamento(self, numero):
        cursor = self.conexion.cursor()
        sqlselect = "select dept_no, dnombre, loc from dept where dept_no=?"
        cursor.execute(sqlselect, (numero))
        row = cursor.fetchone()
        if (not row):
            #DEVOLVER UN NULO
            cursor.close()
            return None
        else:
            #CREAMOS UN NUEVO OBJETO DEPARTAMENTO
            #PARA DEVOLVER
            departamento = Departamento()
            departamento.numero = row.dept_no
            departamento.nombre = row.dnombre
            departamento.localidad = row.loc
            cursor.close()
            return departamento

    def todosDepartamentos(self):
        cursor = self.conexion.cursor()
        sqlselect = "select dept_no, dnombre, loc from dept"
        cursor.execute(sqlselect)
        #Creamos una lista para devolver todos los departamentos
        departamentos = []
        for row in cursor:
            #Creamos un departamento por cada fila del bucle
            dept = Departamento()
            #Asignamos los datos al nuevo objeto dept
            dept.numero = row.dept_no
            dept.nombre = row.dnombre
            dept.localidad = row.loc
            #Añadimos a la lista cada nuevo objeto dept
            departamentos.append(dept)
        cursor.close()
        return departamentos