from os import system
from pathlib import Path
import os

def mostrar_opciones_menu():
    print('1 - Leer receta\n2 - Crear receta\n3 - Crear categoría\n4 - Eliminar receta\n5 - Eliminar categoría\n6 - Cerrar recetario')

def total_recetas(ruta_base, ruta):
    total_recetas = Path(ruta_recetas).glob('**/*.txt')
    return total_recetas

def mostrar_recetas():
    recetas = total_recetas(ruta_base, ruta_recetas)
    nombre_receta = ''
    numero_receta = 1
    for receta in recetas:
        nombre_receta = str(numero_receta) + ' - ' + receta.stem
        print(nombre_receta)
        numero_receta += 1

def leer_receta():
    mostrar_recetas()
    numero_seleccionar_receta = int(input('Selecciona una receta: '))
    recetas = total_recetas(ruta_base, ruta_recetas)
    lista_recetas = []
    numero_receta = 0

    for receta in recetas:
        lista_recetas.append(receta.absolute())
        numero_receta += 1
    
    system('cls')
    
    texto_receta = open(lista_recetas[numero_seleccionar_receta-1])
    print(texto_receta.read())
    texto_receta.close()

def mostrar_categorias():
    lista_categorias = os.listdir(ruta_recetas)
    for categoria in lista_categorias:
        print(' - ' +categoria)

def crear_receta():
    nombre_fichero_receta = input('Nombre de la receta: ')
    nombre_fichero_receta += '.txt'
    texto_receta = input('Descripción de la receta: ')
    
    mostrar_categorias()
    
    categoria_receta = input('Categoría de la receta: ')
    os.chdir(str(ruta_recetas) + '\\' + categoria_receta)
    
    receta = open(nombre_fichero_receta, 'x')
    receta.write(texto_receta)
    receta.close()
    
    system('cls')
    
def crear_categoria():
    print('Estas son las categorías que ya existen:')
    mostrar_categorias()
    nombre_categoria = input('Nombre de la categoría: ')
    
    os.mkdir(str(ruta_recetas) + '\\' + nombre_categoria)
    
    system('cls')
    
def eliminar_receta():
    mostrar_recetas()
    numero_receta_eliminar = int(input('Elige la receta que quieres eliminar: '))
    recetas = total_recetas(ruta_base, ruta_recetas)
    lista_recetas = []
    numero_receta = 0

    for receta in recetas:
        lista_recetas.append(receta.absolute())
        numero_receta += 1

    ruta_eliminar_receta = lista_recetas[numero_receta_eliminar-1]
    os.remove(ruta_eliminar_receta)
    
    system('cls')
    
    mostrar_recetas()

def eliminar_categoria():
    mostrar_categorias()
    categoria_eliminar = input('Elige la categoría que quieres eliminar: ')

    os.rmdir(str(ruta_recetas) + '\\' + categoria_eliminar)
    
    system('cls')
    
    mostrar_categorias()


ruta_base = Path.home()
ruta_recetas = Path(ruta_base, 'Desktop', 'Python Udemy', 'dia_6', 'Recetas')
numero_total_recetas = len(list(total_recetas(ruta_base, ruta_recetas)))

print('Bienvenido al recetario!')
print(f'Las recetas están almacenadas en: {ruta_recetas}')
print(f'Hay un total de {numero_total_recetas} recetas')
mostrar_opciones_menu()
opcion_menu_elegida = int(input('Elige una opción: '))

while opcion_menu_elegida != 6:
    match opcion_menu_elegida:
        case 1:
            system('cls')
            leer_receta()
            break
        case 2:
            system('cls')
            crear_receta()
            break
        case 3:
            system('cls')
            crear_categoria()
            break
        case 4:
            system('cls')
            eliminar_receta()
            break
        case 5:
            system('cls')
            eliminar_categoria()
            break
        case 6:
            system('cls')
            print('Hasta pronto!')
            break
        case _:
            system('cls')
            mostrar_opciones_menu()
            opcion_menu_elegida = int(input('Escribe una opción válida: '))
        