def isBisiesto(anyo):
   if (anyo%4 == 0):
       if (anyo%100 != 0 or anyo%400 == 0):
           print("BISIESTO")
       else:
           print("no es bisiesto")
   else:
       print("No es bisiesto")