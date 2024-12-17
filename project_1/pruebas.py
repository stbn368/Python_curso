import re

def verificar_email(email):
    if not re.search(r'.*@.*\.com$', email) == None:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


def verificar_saludo(frase):
    if not re.search(r'^h|Hola', frase) == None:
        print("Ok")
    else:
        print("No has saludado")
        

def verificar_cp(cp):
    if not re.search(r'\w{2}\d{4}', cp) == None:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


