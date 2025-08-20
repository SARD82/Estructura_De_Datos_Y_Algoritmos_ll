""" Se tienen 2 arreglos de tamaño 11 cada uno, y que contienen elementos que no se repiten, hacer un programa que lea y ordene (con burbuja) en el arreglo C, a los arreglos A y B, además se deberá imprimir el tiempo que tarda el programa en realizar dicha tarea. Se debe escribir previamente un Algoritmo para la solución"""

print("Programa que ordena con Bubble Sort dos arreglos en uno y mide el tiempo de ejecución")

import random
import time

# Creación de arreglos
print("-----------------------------------------------------------------------------")
A = random.sample(range(1, 12), 11) # Para crear arreglos con 11 elementos aleatorios, el rango de que número a que número va a ser y el número de elementos que va a contener el arreglo
B = random.sample(range(12, 23), 11)
C = A + B

# Impresión de arreglos
print("-----------------------------------------------------------------------------")
print(A)
print(B)
print(C)

# Operaciones
inicio = time.time()

# Bubble Sort
for i in range(1, len(C)):
    print("PASADA ", i)
    for j in range(len(C) - 1):
        if C[j] > C[j + 1]:
            temp = C[j]
            C[j] = C[j + 1]
            C[j + 1] = temp
        print(C)
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion: .6f} segundos")