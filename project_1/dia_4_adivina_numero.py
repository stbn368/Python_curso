import random

def generar_numero_nivel__tope_rango (nivel_elegido):
    # genera un número random y el número tope del rango según el nivel
    if nivel_elegido == 'principiante':
        tope_rango = 10
        numero_nivel = random.randint(1, 10)
    elif nivel_elegido == 'medio':
        tope_rango = 100
        numero_nivel = random.randint(1, 100)
    else:
        tope_rango = 1000
        numero_nivel = random.randint(1, 1000)
    #devuelve una lista con los dos valores generados
    return [numero_nivel, tope_rango]

def ejecutar_nivel (nivel_elegido, intentos):
    # ejecuta el juego en función del nivel y los intentos que se le haya pasado
    nivel__tope_rango = generar_numero_nivel__tope_rango(nivel_elegido)
    ganador = False

    while intentos > 0:
        try:
            numero_elegido = int(input(f"Elige un número entre: 1 - {nivel__tope_rango[1]}\nTienes {intentos} intentos: "))
            intentos -= 1
            if numero_elegido < 1 or numero_elegido > nivel__tope_rango[1]:
                print(f"El número debe estar dentro del rango 1 - {nivel__tope_rango[1]}")
            elif numero_elegido == nivel__tope_rango[0]:
                print(f"Enhorabuena, has acertado el número {nivel__tope_rango[0]} y te han sobrado {intentos}")
                ganador = True
                break
            elif numero_elegido < nivel__tope_rango[0]:
                print("El número debe ser mayor...")
            elif numero_elegido > nivel__tope_rango[0]:
                print("El número debe ser menor...")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
    return ganador


salir_juego = False
#inicio menu del juego
while not salir_juego:
    nivel = input("Empieza el juego 'Adivina el número'\nElige el nivel:\n\tPrincipiante\n\tMedio\n\tAvanzado\n\t***\n\tSalir\n")

    match nivel.lower():
        case 'principiante':
            if ejecutar_nivel(nivel.lower(), 5):
                break
            else:
                print("Has perdido, ¿quieres intentarlo de nuevo?")
        case 'medio':
            if ejecutar_nivel(nivel.lower(), 8):
                break
            else:
                print("Has perdido, ¿quieres intentarlo de nuevo?")
        case 'avanzado':
            if ejecutar_nivel(nivel.lower(), 10):
                break
            else:
                print("Has perdido, ¿quieres intentarlo de nuevo?")
        case 'salir':
            salir_juego = True
            print("Gracias por jugar!")
            break
        case _:
            print("Escribe una opción válida.\n")



