"""Programa que solicite al usuario un número entero positivo, y utilizando ciclos que imprima los siguientes patrones, por ejemplo N = 10
*
**
***
****
*****
******
*******
********
*********
**********"""

print("Programa que genera patrones en forma de medio triángulos")

# Input de datos
print("-----------------------------------------------------------------------------")
n = int(input("Ingrese la cantidad de '*' que llevara la base del triángulo: "))

# Cálculo de datos
print("-----------------------------------------------------------------------------")
for i in range(n):
    cantidad = '*'
    # Impresión
    print((i + 1) * cantidad)