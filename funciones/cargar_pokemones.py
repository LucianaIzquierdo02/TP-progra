import json

def cargar_pokemones() -> dict:
    """ Carga los datos de cada Oikemón desde un archivo JSON """
    
    try:
        with open("pokemones.json", "r") as archivo:
            pokemones = json.load(archivo)
        return pokemones
    except FileNotFoundError:
        print("Error: el archivo pokemones.json no se encontró.")


""" 
json.load(): Este método lee el contenido de un archivo y lo convierte a su correspondiente estructura en Python (como diccionarios, listas, cadenas, números, etc.).
"""