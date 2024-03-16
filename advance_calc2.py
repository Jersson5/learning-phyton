'''Calculadora que reciba 2 numeros
y realice la operacion aritmetica que el usuario desee
Puede escoger +,-,*,/.
'''
import os
os.system("clear")

def calculator(x, y, z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y 
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return 'No es posible entre cero caballo(a)'
        else: x / y
    else : 
        return 'Funcion invalida caballo(a)'
n1 = float(input("Ingrese el primer valor"))
n2 = float(input("Ingrese el segundo valor"))

print("_______MENU CALCULADORA________")
print("[1.] Sumar")
print("[2.] Restar")
print("[3.] Multiplicar")
print("[4.] Dividir")
print("[5.] TODAS")
opc = input("Digite una opcion del menu")

ans = calculator(n1, n2, opc)
print("Resultado: ", ans)