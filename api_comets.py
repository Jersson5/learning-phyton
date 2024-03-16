'''
Script description: Get all date abouts comets.
'''

import requests

def get_comets():
    global count 
    print("___COMET INFORMATION___")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    

    try: 
        #Requests to API
        response = requests.get(url)
        response.raise_for_status()

        #Print comets names
        data = response.json()
        count = 0
        #total = int(input("Cantidad de datos a mostrar: "))
        planet = input("Escriba el planeta a buscar: ")

        for comet in data["bodies"]:
            #if comet ["isPlanet"] == True:
            if comet ["englishName"] == planet:

                print("English name: ", comet["englishName"])
                print("Moons: ", comet["moons"])
                print("Gravity: ", comet["gravity"])
                print("Is planet?: ", comet["isPlanet"])
                print("/n")

                '''count = count + 1
            if count == total:
                break
        print(count)'''

    except requests.exceptions.RequestException as e:
        print(f"API ERROR: {e}")

#Call function
get_comets()