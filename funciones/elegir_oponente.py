import random
from funciones.crear_pokemon import crear_pokemon
from funciones.cargar_pokemones import cargar_pokemones

#Elige un oponente aleatorio para el jugador
def elegir_oponente() -> dict:
    
    pokemones = cargar_pokemones()
    
    print("Tu oponente es elegido aleatoriamente:")
    
    
    # Obtener las claves de los oponentes disponibles
    oponentes = pokemones["oponentes"]
    
    # Elegir una opción aleatoria de entre las claves del diccionario
    # explicación ----->
    # oponentes.keys(): es un objeto de tipo dict_keys, que se ve como una lista, pero no es una lista propiamente dicha. Keys() es un método de los diccionarios en Python que devuelve una vista de todas las claves en el diccionario
    # a función list() convierte el objeto dict_keys en una lista estándar de Python
    # list(oponentes.keys()): ['1', '2', '3', '4']
    opcion = random.choice(list(oponentes.keys()))
    
    # Obtener el oponente elegido
    oponente_elegido = oponentes[opcion]
    
    # Crear el diccionario completo del oponente con HP
    oponente_elegido = crear_pokemon(oponente_elegido["nombre"], oponente_elegido["tipo"], oponente_elegido["ataques"])
    
    print(f"Tu oponente es: {oponente_elegido['nombre']} (Tipo: {oponente_elegido['tipo']})")
    
    return oponente_elegido