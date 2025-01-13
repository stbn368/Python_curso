import random
import os

def elegir_palabra():
    banco_palabras = ['nivel', 'agua', 'astronauta', 'tiempo', 'año', 'dia', 'escuela', 'familia', 'pais', 'problema', 'lugar','empresa', 'gobierno', 'tipo', 
                      'lado', 'asunto', 'negocio', 'libro', 'estudio', 'area', 'madre', 'agua', 'punto', 'numero', 'servicio', 'amigo', 'hora', 'ciudad', 'idea', 
                      'informacion', 'padre', 'rostro', 'persona', 'fiesta', 'llamar', 'dar', 'encontrar', 'mirar', 'hacer', 'querria', 'obtener', 'tener', 
                      'chica', 'razon', 'cambio', 'preguntar', 'sentir', 'poner', 'significar', 'empezar', 'hablar', 'podria', 'jugar', 'mover', 'gustar', 'servir', 
                      'esperar', 'leer', 'hablar', 'crear', 'mirar', 'guiar', 'establecer', 'pagar', 'perder', 'creer', 'esperar', 'construir', 'matar', 'primero', 
                      'largo', 'pequeño', 'proximo', 'importante', 'publico', 'real', 'religioso', 'similar', 'popular', 'comun', 'unico', 'nacional', 'verdadero', 
                      'especial', 'politico', 'europeo', 'politico', 'legal', 'medico', 'bueno', 'positivo', 'grande', 'joven', 'importante', 'fuerte', 'varios', 
                      'actual', 'gratis', 'alto', 'rojo', 'bueno']
    
    palabra_elegida = random.choice(banco_palabras)
    return palabra_elegida

def generar_hueco(palabra):
    return '¬' * len(palabra)

def generar_intentos(palabra):
    return max(len(palabra), 10)

def pedir_letra():
    letra = input('Elige una letra: ')
    if len(letra) == 1:
        return letra.lower()
    else:
        print('Introduce solo un carácter.')
        return pedir_letra()

def analizador_palabra (letra, palabra):
    return [l if l == letra else '¬' for l in palabra]

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    palabra_original = elegir_palabra()
    intentos = generar_intentos(palabra_original)
    huecos_palabra = generar_hueco(palabra_original)

    print(f'La palabra tiene {len(huecos_palabra)} letras:')
    print(huecos_palabra)

    palabra_analizada = []
    almacen_letras = []
    palabra_final = list(huecos_palabra)
    indice_letra = -1
    acierto = False

    while intentos > 0:
        print(f'Tienes {intentos} intentos.')
        letra = pedir_letra()
        
        if letra in almacen_letras:
            print('Ya has usado esa letra.')
            continue
        else:
            almacen_letras.append(letra)
            
        palabra_analizada = analizador_palabra(letra, palabra_original)

        for l in palabra_analizada:
            indice_letra += 1
            if l != '¬':
                palabra_final.pop(indice_letra)
                palabra_final.insert(indice_letra, l)
                acierto = True
            else:
                pass
        if not acierto:
            intentos -= 1
        
        acierto = False
        indice_letra = -1
        
        limpiar_consola()
        
        print(f'Letras usadas: {almacen_letras}')
        print(''.join(palabra_final))

        if palabra_original == ''.join(palabra_final):
            print(f'Enhorabuena! Has acertado --> {palabra_original}')
            break
    if intentos == 0 and palabra_original != ''.join(palabra_final):
        print(f'Suerte la próxima vez... --> {palabra_original}')

if __name__ == "__main__":
    main()