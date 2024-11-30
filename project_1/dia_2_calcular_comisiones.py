#Ejercicio para calcular comisiones de un trabajdor y mostrarlo por pantalla

nombre = input("¿Cómo te llamas? ")
ventas = input("¿Cuánto has vendido este mes (€)? ")
resultado_comisiones = round(float(ventas) * 0.15, 2)

print(f"Hola {nombre}, tus ganancias en comisiones este mes han sido {resultado_comisiones}")