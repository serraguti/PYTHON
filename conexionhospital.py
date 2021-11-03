import pyodbc
servidor = "LOCALHOST"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"


class ConexionHospital:
    # En el constructor, creará una conexión
    # para poder trabajar con cualquier método
    # de consultas que tengamos
    def __init__(self):
        # self se refiere a la clase en la que estamos
        # escribiendo
        # En esta clase, nos creamos una propiedad llamada
        # conexion
        self.conexion = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server="
                                       + servidor + "; Database=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

     # Vamos a realizar un método para eliminar enfermo
    def eliminarEnfermo(self, inscripcion):
        # Entrar y salir
        cursor = self.conexion.cursor()
        sqldelete = "delete from enfermo where inscripcion=?"
        cursor.execute(sqldelete, (inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados

    def modificarEnfermo(self, apellido, inscripcion):
        #Entrar y salir
        cursor = self.conexion.cursor()
        #Escribimos la consulta
        sqlupdate = "update enfermo set apellido=? where inscripcion=?"
        cursor.execute(sqlupdate, (apellido, inscripcion))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados