print("Ejemplo ficheros Python")
#Vamos a crear un nuevo archivo y escribimos algo en él
#Voy a utilizar w+ que Lectura/Escritura
fichero = open("nombre.txt", "w+")
print("Introduzca su nombre")
nombre = input()
fichero.write("Su nombre es..." + nombre)
#Es recomendable utilizar FLUSH para escribir
#en un archivo, lo que hace es liberar la memoria 
#despues de escribir.
#Sirve cuando guardamos mucho contenido
fichero.flush()
#Cerramos el fichero
fichero.close()
#Añadimos un valor al archivo nuevo
#Lo abrimos para añadir
archivo = open("nombre.txt", "a")
print("Introduzca otro nombre")
nombre = input()
archivo.write("\n" + nombre)
archivo.close()
#Vamos a abrir el archivo y leemos su contenido
file = open("nombre.txt", "r")
contenido = file.read()
print(contenido)
file.close()
print("Fin de programa")