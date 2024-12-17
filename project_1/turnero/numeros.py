#generador turnos perfumería
def generador_p():
    turno = 1
    while True:
        yield f"P - {turno}"
        turno += 1

generador_perfumeria = generador_p()

#generador turnos farmacia
def generador_f():
    turno = 1
    while True:
        yield f"F - {turno}"
        turno += 1

generador_farmacia = generador_f()


#generador turnos cosméticos
def generador_c():
    turno = 1
    while True:
        yield f"C - {turno}"
        turno += 1

generador_cosmetico = generador_c()


#decorador
def decorador(opcion):
    print("Su turno es: ")
    if opcion == "p":
        print(next(generador_perfumeria))
    elif opcion == "f":
        print(next(generador_farmacia))
    elif opcion == "c":
        print(next(generador_cosmetico))
    print("Espera en la cola.")
        
    
