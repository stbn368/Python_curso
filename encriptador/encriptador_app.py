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

def main():
    print('[1] - Encriptar\n[2] - Desemcriptar')
    try:
        option_elegida = int(input('Elige una opción: '))
    except ValueError:
        print('Valor incorrecto.')
        return

    if option_elegida == 1:
        # Encriptar el archivo
        ruta_archivo = input('Introduce la ruta y el nombre del fichero: ')
        try:
            encriptar_archivo(ruta_archivo)
            print(f"El archivo {ruta_archivo} ha sido encriptado.")
        except Exception as e:
            print(f"Error al encriptar el archivo: {e}")
        
    elif option_elegida == 2:
        # Desencriptar el archivo
        ruta_archivo = input('Introduce la ruta y el nombre del fichero: ')
        try:
            desencriptar_archivo(ruta_archivo)
            print(f"El archivo {ruta_archivo} ha sido desencriptado.")
        except Exception as e:
            print(f"Error al desencriptar el archivo: {e}")
    else:
        print('Opción incorrecta.')

if __name__ == "__main__":
    main()

