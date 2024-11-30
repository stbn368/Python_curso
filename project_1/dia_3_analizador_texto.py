texto = input('Introduce tu texto: ')
texto_mayusculas = texto.upper()

#declaración de lista vacía
letras = []
print('Introduce 3 letras: ')
letras.append(input('Primera letra: '))
letras.append(input('Segunda letra: '))
letras.append(input('Tercera letra: '))

letra_1_mayusculas = letras[0].upper()
letra_2_mayusculas = letras[1].upper()
letra_3_mayusculas = letras[2].upper()

palabras_en_texto_original = texto.split(' ')
palabras_en_texto_mayusculasusculas = texto_mayusculas.split(' ')

signos_validos = ['.', ',', ';', ':', '!', '?']
palabra_buscada = 'PYTHON'

print('***********************************************')

#transformar lista en string en orden inverso
palabras_en_texto_orden_inverso = ' '.join(palabras_en_texto_original[::-1])
print('***********************************************')

#mostrar recuento de letras en texto
print(f'La letra {letras[0]} aparece {texto_mayusculas.count(letra_1_mayusculas)}.\nLa letra {letras[1]} aparece {texto_mayusculas.count(letra_2_mayusculas)}.\nLa letra {letras[2]} aparece {texto_mayusculas.count(letra_3_mayusculas)}.')
print('***********************************************')

#mostrar el número de palabras que hay en el texto
print(f'En el texto hay {len(palabras_en_texto_original)} palabras.')
print('***********************************************')

#mostrar la primera y última letra del texto
print(f'La primera letra es {texto[0]}.\nLa última letra es {texto[-1]}.')
print('***********************************************')

#mostrar el texto con las palabras en orden inverso
#también se podrías hacer con el método reverse() => texto.reverse()
print(f'Texto con palabras en orden inverso: {palabras_en_texto_orden_inverso}')
print('***********************************************')

#comprobar si aparece la palabra Python en el texto
print('¿Aparece la palabra "Python"?')
verificador = False
for s in signos_validos:
    if (palabra_buscada + s) in palabras_en_texto_mayusculasusculas:
        print('Si aparece!')
        verificador = True
        break

if verificador == False:
    print('No aparece!')

