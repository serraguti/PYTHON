import pyodbc
from conexionhospital import ConexionHospital

print("Escriba una inscripción de enfermo para eliminar")
inscripcion = int(input())
#AQUI GESTIONAMOS LA CONSULTA DE ACCION CON LA CLASE DE CONEXION
#CREAMOS UN NUEVO OBJETO PARA LAS ACCIONES DE BBDD
connection = ConexionHospital()
#QUEREMOS ELIMINAR Y NOS DEVUELVE UN NUMERO
respuesta = connection.eliminarEnfermo(inscripcion)
print("Registros eliminados " + str(respuesta))
#A continuacion, vamos a pedir modificar el apellido
# de un enfermo por su inscripcion
#Necesitamos pedir el apellido y la inscripcion
print("Introduzca una inscripcion para modificar")
ins = int(input())
print("Introduzca el nuevo apellido")
ape = input()
respuesta = connection.modificarEnfermo(ape, ins)
print("Registros modificados: " + str(respuesta))
print("Fin de programa")
