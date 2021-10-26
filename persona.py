class Persona:
    nombre = ""
    apellidos = ""
    fechanacimiento = 0
    pais = ""
    def __str__(self):
        return self.nombre + " " + self.apellidos + ", Pais " + self.pais + ", Edad: " + str(self.getEdad())

    #Un constructor es un metodo donde se inician
    #las variables de un objeto o se le indican
    #elementos cuando se construye un objeto
    #Es el primer metodo que se lee en cualquier clase
    def __init__(self):
        #Aqui indicamos como deseamos que sea el objeto
        #Yo quiero que cualquier Persona sea de Francia
        #al iniciar, luego si quiere, que cambie.
        self.pais = "Francia"
    #Por ejemplo, pongamos que queremos mostrar 
    #el nombre y apellidos de una persona en un método
    def getNombreCompleto(self):
        #Nuestro código
        return self.nombre + " " + self.apellidos

    def getEdad(self):
        #Podemos hacer lo que deseemos, por ejemplo
        #indicar la edad a partir de una propiedad
        return 2021 - self.fechanacimiento

    #Esto son metodos de clase, la unica condición debe
    #ser que reciban SIEMPRE self, pero podemos recibir 
    #mas parametros
    def getDescripcion(self, midescripcion):
        return self.getNombreCompleto() + ", " + midescripcion