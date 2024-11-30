import random

def obtener_respuestas():
    while True:
        # Preguntas para crear el nombre con las respuestas
        print("Responde a las siguientes preguntas para crear el nombre para tu cerveza:")
        cadena1 = input("¿Es rubia o oscura? ")
        cadena2 = input("¿Es amarga o dulce? ")
        cadena3 = input("¿Cuánto tiempo en días de fermentación tiene? ")

        # Verificar que las respuestas sean lo suficientemente largas
        if min(len(cadena1), len(cadena2), len(cadena3)) > 2:
            return cadena1, cadena2, cadena3
        else:
            print("Las respuestas deben ser más largas...")

def numero_aleatorio_cadena(longitud_cadena):
    return random.randint(0, longitud_cadena - 1)

def generar_cadena_aleatoria(cadena):
    while True:
        #utilizando una lista por comprensión
        cadena_random = "".join([c for c in cadena if numero_aleatorio_cadena(len(cadena)) == cadena.index(c)])
        if len(cadena_random) > 1:
            return cadena_random

def main():
    cadena1, cadena2, cadena3 = obtener_respuestas()
    nombre_cerveza = generar_cadena_aleatoria(cadena1) + generar_cadena_aleatoria(cadena2) + generar_cadena_aleatoria(cadena3)
    print("Nombre final:", nombre_cerveza)

if __name__ == "__main__":
    main()
