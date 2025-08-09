"""print("hola mundo")"""
#import math.sqrt(9)
#print (raiz) 
#ingrese el numero
numero=float(input("INGRESE UN NUMERO POSITIVO: "))
#VERIFICAMOS SI ES UN NUMERO POSITIVO
if numero >= 0:
    raiz = numero ** 0.5 # USAMOS POTENCIA :ELEVAR A 1/2 ES LO MISMO QUE RAIZ CUADRADA
    print (f"La raiz cuadrada de {numero} es:{raiz}")
else:
    print("Error: el numero debe ser positivo.")
