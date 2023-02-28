import random
from queue import Queue
from collections import deque

# Función para generar los números aleatorios
def generar_numeros_aleatorios():
    return [random.randint(-10000000, 10000000) for _ in range(1000000)]

# Función para insertar los números en una pila y extraerlos
def insertar_y_extraer_pila(numeros):
    pila = []
    for numero in numeros:
        pila.append(numero)
    while pila:
        numero = pila.pop()

# Función para insertar los números en una cola y extraerlos
def insertar_y_extraer_cola(numeros):
    cola = deque()
    for numero in numeros:
        cola.append(numero)
    while cola:
        numero = cola.popleft()

# Función principal que muestra el menú y llama a las funciones correspondientes
def main():
    numeros = generar_numeros_aleatorios()
    opcion = input("Ingrese la opción que desea ejecutar:\n1. Insertar y extraer en una pila\n2. Insertar y extraer en una cola\nOpción: ")
    if opcion == "1":
        insertar_y_extraer_pila(numeros)
    elif opcion == "2":
        insertar_y_extraer_cola(numeros)
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()
