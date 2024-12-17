import bs4
import requests

#crear url sin número de página
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

'''resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')'''

'''ejemplo = libros[0].select('p')[0].get_attribute_list('class')[1]
print(ejemplo)'''

#lista vacía para almacenar los títulos
titulos_libros = []
numero_titulos_esperados = 375

#rango en función del número de páginas que hay (50)
for p in range(1, 51):
    #url de cada página
    resultado = requests.get(url_base.format(p))
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar todos los elementos con la clase para identificar los libros
    libros = sopa.select('.product_pod')

    for libro in libros:
        #condición para confirmar si los libros tienen 4 o 5 estrellas
        if libro.select('p')[0].get_attribute_list('class')[1] == 'Four' or \
                libro.select('p')[0].get_attribute_list('class')[1] == 'Five':
            #guardar título si la condición se cumple
            titulos_libros.append(libro.select('a')[1]['title'])

#confirmar que el total de libros encontrados coincide con los libros esperados
if len(titulos_libros) != numero_titulos_esperados:
    raise ValueError(f'Número de títulos esperado: {numero_titulos_esperados}\nNúmero de títulos encontrados: {len(titulos_libros)}')

#mostrar los títulos encontrados
print('Títulos:')

for titulo in titulos_libros:
    print(f'\t{titulo}')

print(f'Total libros: {len(titulos_libros)}')


