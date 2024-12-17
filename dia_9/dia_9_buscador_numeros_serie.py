import shutil
import re
import os
from pathlib import Path

#fichero_comprimido = 'Proyecto+Dia+9.zip'
#fichero_descomprimido = shutil.unpack_archive(fichero_comprimido, 'fichero_descomprimido')

ruta_analizar = 'fichero_descomprimido'
expresion_buscar = r'[N] + [\w{3}] + [-] + [\d{5}]'

def buscador(ruta, expresion):
    lista_archivos = []
    lista_series = []
    
    with open(ruta, 'r') as archivo: 
        contenido = archivo.read()
        coincidencias = re.findall(expresion, contenido)
        
        if coincidencias: 
            print(f'Se encontraron {len(coincidencias)} coincidencias de la cadena "{expresion}":') 
            for coincidencia in coincidencias: 
                print(coincidencia)
    
    #ficheros = Path(ruta).glob('**/*.txt')
    
    #for archivo in ruta:      
    #    if archivo.endswith('.txt'): 
    #        lista_archivos.append(os.path.join(archivo))
                
    return lista_archivos, lista_series

listas_tupla = buscador(ruta_analizar, expresion_buscar)

for lista in listas_tupla:
    for elemento in lista: 
        print(elemento)

                
