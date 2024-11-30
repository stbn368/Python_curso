#Ejercicio para crear un nombre de una cerveza a partir de respuestas introducidas por el usuario
import random

comprobador = True
#Con este bucle while controlamos que las respuestas no sean demasiado cortas y provoquen un bucle infinito cuando genera la cadena aleatoria
while comprobador:
    #Preguntas para crear el nombre con las respuestas
    print("Responde a las siguientes preguntas para crear el nombre para tu cerveza:")
    cadena1 = input("¿Es rubia o oscura? ")
    cadena2 = input("¿Es amarga o dulce? ")
    cadena3 = input("¿Cuánto tiempo en días de fermentación tiene? ")

    #Calcular la longitud de cada cadena y obtener la mínima
    longitud_cadenas = [len(cadena1), len(cadena2), len(cadena3)]
    cadena_pequenia = min(longitud_cadenas)
    
    if cadena_pequenia > 2:
        comprobador = False
    else:
        print("Las respuestas deben ser más largas...")

#Función para generar un número aleatorio teniendo en cuenta la longitud menor de todas las cadenas
def numero_aleatorio_cadena (longitud_cadena):
    if longitud_cadena > 0:
        numero = random.randint(1, longitud_cadena)
        return numero
    else:
        print("La cadena más pequeña tiene longitud 0, no se puede generar un número aleatorio.")

#Función para generar una cadena aleatoria teniendo en cuenta un número aleatorio y una cadena
def generar_cadena_aleatoria (cadena):
    cadena_random = ""
    comprobador = True
    
    #El bucle while hace que el for trabaje hasta que por las coincidencias se cree una cadena de al menos 2 caracteres
    while comprobador:
        for c in cadena:
            if numero_aleatorio_cadena(len(cadena)) == cadena.index(c):
                cadena_random += c
            else:
                print("trabajando...")

        if len(cadena_random) > 1:
            comprobador = False
            return cadena_random

#Mostrar el nombre generando
print("Nombre final: " + generar_cadena_aleatoria(cadena1) + generar_cadena_aleatoria(cadena2) + generar_cadena_aleatoria(cadena3))