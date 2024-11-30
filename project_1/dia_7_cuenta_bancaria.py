from os import system
import random

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    
    lista_clientes = []
    
    def __init__(self, id, nombre, apellido, numero_cuenta, saldo = 0.0):
        super().__init__(nombre, apellido)
        self.id = id
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
     
    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nSaldo en cuenta {self.numero_cuenta}: {self.saldo}'
        
    def mostrar_saldo(self):
        print(f'Saldo: {self.saldo}')
    
    def mostrar_numero_cuenta(self):
        print(f'Número de cuenta: {self.numero_cuenta[0], 
              self.numero_cuenta[1],
              self.numero_cuenta[2],
              self.numero_cuenta[3]}')
    
    def mostrar_nombre(self):
        return self.nombre

    def ingresar_dinero(self, cantidad_dinero):
        if cantidad_dinero <= 0:
            print('Tienes que ingresar una cantidad positiva o mayor que 0')
        else:
            self.saldo += cantidad_dinero
    
    def retirar_dinero(self, cantidad_dinero):
        if self.saldo == 0:
            print('No tienes saldo en la cuenta.')
        elif self.saldo < cantidad_dinero and self.saldo > 0:
            print('No tienes suficiente saldo en la cuenta.')
        else:
            self.saldo -= cantidad_dinero

def id_cliente_aleatorio ():
    numero = random.randint(1, 99999)
    return numero

def numero_cuenta_cliente_aleatorio ():
    numero = random.randint(1, 999)
    return numero
        
def crear_cliente():
    nombre_cliente = input('Introduce tu nombre: ')
    apellido_cliente = input('Introduce tu apellido: ')
    
    id_cliente = id_cliente_aleatorio()
    
    numero_cuenta_cliente = [numero_cuenta_cliente_aleatorio(), 
                            numero_cuenta_cliente_aleatorio(), 
                            numero_cuenta_cliente_aleatorio(), 
                            numero_cuenta_cliente_aleatorio()]
    
    #nuevo_cliente = Cliente(id_cliente, nombre_cliente, apellido_cliente, numero_cuenta_cliente)
    nuevo_cliente = (Cliente(id_cliente, nombre_cliente, apellido_cliente, [numero_cuenta_cliente])) 
    return nuevo_cliente

# Añadir un cliente administrador a la lista 
Cliente.lista_clientes.append(Cliente(id_cliente_aleatorio(), 'Admin', 'AdminA', [numero_cuenta_cliente_aleatorio(), numero_cuenta_cliente_aleatorio(), numero_cuenta_cliente_aleatorio(), numero_cuenta_cliente_aleatorio()])) 

#menu
def menu_inicio():
    print('Elige una opción:\n\t[1] - Crear cliente\n\t[2] - Consultar datos\n\t[3] - Ingresar dinero\n\t[4] - Retirar dinero\n\t[5] - Consultar saldo\n\t[6] - Salir')
    opcion_elegida = input()
    return int(opcion_elegida)

salir_programa = False

while not salir_programa:
    match menu_inicio():
        case 1:
            system('cls')
            Cliente.lista_clientes.append(crear_cliente())
        case 2:
            system('cls')
            nombre_cliente = (input('Introduce un nombre: '))
            clientes_encontrados = [cliente for cliente in Cliente.lista_clientes if nombre_cliente in cliente.mostrar_nombre()]
            for cliente in clientes_encontrados: 
                if cliente.mostrar_nombre == nombre_cliente:
                    print(cliente)
                else:
                    print('Ese cliente no existe.')
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Hasta la próxima!")
            salir_programa = True
            break
        case _:
            print("Escribe una opción válida.\n")




'''while opcion_elegida == 0:
    cliente1 = Cliente(10, 'Esteban', 'Calderon', '123', 25)
    cliente2 = Cliente(11, 'Gloria', 'Bayon', '333', 12)
    #cliente3 = crear_cliente()
    
    lista_clientes = [cliente1, cliente2]
    
    print('cantidad de clientes: ' + str(len(lista_clientes)))
    
    lista_clientes.append(crear_cliente())
    
    print('cantidad de clientes: ' + str(len(lista_clientes)))
    
    print(str(lista_clientes[2].id) + '\n' +
          str(lista_clientes[2].mostrar_numero_cuenta()))
    
    lista_clientes[2].mostrar_saldo()
    
    lista_clientes[2].ingresar_dinero(int(input('¿Cuánto quieres ingresar? ')))
    
    lista_clientes[2].mostrar_saldo()
    
    lista_clientes[2].retirar_dinero(int(input('¿Cuánto quieres retirar? ')))
    
    lista_clientes[2].mostrar_saldo()
    
    #print(cliente3.id)
    #print(cliente3.mostrar_saldo())
    #print(cliente3.mostrar_numero_cuenta())
    
    opcion_elegida = input('Elige una opción: ')'''



