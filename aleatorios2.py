'''Script descripcion:
Cree una funcion que genere el lanzamineto de dos dados (1-6) 
y que muestre en pantalla el mensaje ganador
sino dira el mensaje sigue intentando'''

#Importo biblioteca para generar numeros aleatorios enteros
from random import randint

#Lanzar y generar los valores de los dados
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2
#SALIDAS    
d = dices()  
d1 = d[0]
d2 = d[0]  

#print ("Dados: ", d)
print ("Dados 1: ", d[0])
print ("Dados 2: ", d[1])
#print("El resultado del dado1 es: ", dice1)
#print("El resultado del dado2 es: ", dice2)

