import random

def juego_de_numeros():
    print("Bienvenido al juego de numeros")

    numero_secreto= random.radint([1, 100])

    intentos = 0
    adivinado = False

    print("Intenta adivinar el numero entre 1 y 100")
    while not adivinado:
        try:
            suposición = int(input("Tu suposición: "))
            intentos +=1
            if suposición == numero_secreto:
                adivinado = True
                print(f"Correcto Has adivinado el numero en {intentos} intentos. ")
            elif suposición < numero_secreto:
                print("El numero es mayor. Intenta nuevamente.")
            else: 
                print("El numero es menor intenta nuevamente")

        except ValueError:
            print("Por favor, ingresa un numero valido")

juego_de_numeros()
