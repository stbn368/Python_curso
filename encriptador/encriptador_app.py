from cryptography.fernet import Fernet
import os

# Generar una clave y guardarla en un archivo
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_archivo:
        clave_archivo.write(clave)

# Cargar la clave desde el archivo
def cargar_clave():
    return open("clave.key", "rb").read()

# Encriptar un archivo
def encriptar_archivo(nombre_archivo):
    clave = cargar_clave()
    fernet = Fernet(clave)
    
    with open(nombre_archivo, "rb") as archivo:
        archivo_datos = archivo.read()
    
    archivo_encriptado = fernet.encrypt(archivo_datos)
    
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(archivo_encriptado)

# Desencriptar un archivo
def desencriptar_archivo(nombre_archivo):
    clave = cargar_clave()
    fernet = Fernet(clave)
    
    with open(nombre_archivo, "rb") as archivo:
        archivo_encriptado = archivo.read()
    
    archivo_desencriptado = fernet.decrypt(archivo_encriptado)
    
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(archivo_desencriptado)

# Generar y guardar la clave (solo la primera vez)
# generar_clave()

# Ruta del archivo a encriptar/desencriptar
#ruta_archivo = "C:\\Users\\stbn_\\Desktop\\Automation_Python\\u_notes_ignore\\Jenkins_user.txt"

print('[1] - Encriptar\n[2] - Desemcriptar')
option_elegida = int(input('Elige una opción: '))

if option_elegida == 1:
    # Encriptar el archivo
    ruta_archivo = input('Introduce la ruta y el nombre del fichero: ')
    encriptar_archivo(ruta_archivo)
    print(f"El archivo {ruta_archivo} ha sido encriptado.")
elif option_elegida == 2:
    # Desencriptar el archivo
    ruta_archivo = input('Introduce la ruta y el nombre del fichero: ')
    desencriptar_archivo(ruta_archivo)
    print(f"El archivo {ruta_archivo} ha sido desencriptado.")
else:
    print('Opción incorrecta.')



