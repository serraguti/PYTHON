import datetime
print("Conjetura Collatz")
print("Introduzca un número")
today = datetime.date.today()
year = today.year
print(year)
potencia=pow(2,3)
print(potencia)
numero = int(input("prompt: "))
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 + 1
    print(numero)
print("Fin de programa")    
print("Pulse ENTER para finalizar")
input()    

