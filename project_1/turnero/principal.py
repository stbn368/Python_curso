from numeros import *

def menu(opcion_elegida):
    seguir_programa = True
    match opcion_elegida:
            case 1:
                decorador("p")
                otro_turno = nuevo_turno()
                if otro_turno.lower() == "s":
                    pass
                else:
                    print("Hasta pronto!")
                    seguir_programa = False
            case 2:
                decorador("f")
                otro_turno = nuevo_turno()
                if otro_turno.lower() == "s":
                    pass
                else:
                    print("Hasta pronto!")
                    seguir_programa = False
            case 3:
                decorador("c")
                otro_turno = nuevo_turno()
                if otro_turno.lower() == "s":
                    pass
                else:
                    print("Hasta pronto!")
                    seguir_programa = False
            case 4:
                print("Hasta pronto!")
                seguir_programa = False
            case _:
                print("Escribe una opción válida.\n")
            
    return seguir_programa

def lanzar_menu():
    print("\t[1] Perfumería\n\t[2] Farmácia\n\t[3] Cosméticos\n\t[4] Salir")
    departamento_elegido = int(input("¿De qué departamento quieres sacar turno: "))
    return departamento_elegido

def nuevo_turno():
    opcion_nueva = input("¿Quieres otro turno? (s/n): ")
    return opcion_nueva

activado = True
while activado:
    activado = menu(lanzar_menu())

