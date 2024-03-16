'''API: Application Programming Interface
Nasa API: https://api.nasa.gov/
API_KEY_NASA: 8haf9dyjSpTYJ915evaGSa4mOdfuJd8rGx3MtNdp
Developer: Jersson Solarte
Date: 24/01/2024 
Script description: Get data from NASA API about comets
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key=8haf9dyjSpTYJ915evaGSa4mOdfuJd8rGx3MtNdp'''

import requests
import os

os.system('clear')

def get_comet_data(api_key):
    print("___COMET INFORMATION___")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        #Realizar la solicitud a la API
        response = requests.get(url)
        response.raise_for_status() #-> valida si se presenta algun error en la petición
        #Convertir la respuesta a formato JSON o JERSSON xD (JS Object Notation)
        datos = response.json()
        
        print(f"Comet name {datos['name']}")
        print(f"Magnitud absoluta {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max (KM): {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición de la API de la NASA: {e}")


api_key_nasa = '8haf9dyjSpTYJ915evaGSa4mOdfuJd8rGx3MtNdp'
get_comet_data(api_key_nasa)
