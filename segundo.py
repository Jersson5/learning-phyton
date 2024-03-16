def example():
    ans = 0
    operar = True

    while operar:
        try:
            numero = float(input("Ingresa"))
            ans += numero

            if numero == 0:
                operar = False
            else:
                print(ans)
        except ValueError:
            print("Error.")
    print(ans)

    example()