#Necesitamos importar la clase Persona
#import persona
from persona import Persona

print("Ejemplo clases Persona")
#Creamos una nueva persona
person = Persona()
print("Pais " + person.pais)
person.pais = "España"
print("Pais " + person.pais)
#Cambiamos sus propiedades
person.nombre = "Alumno"
person.apellidos = "Azure"
person.fechanacimiento = 1984
print(person.getDescripcion("Soy un buen estudiante"))
# #Podemos llamar a métodos
print(person.getNombreCompleto())
# print("Edad " + str(person.getEdad()))
print(person)


