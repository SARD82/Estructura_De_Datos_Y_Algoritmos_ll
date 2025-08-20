#Programa que resuelva ecuaciones de segundo grado, debe tomar en cuenta raices reales y complejas, el usuario solo proporciona (a,b,c).

import numpy as np

print("Programa que resuelve ecuaciones de segundo grado")

# Input de datos
print("-----------------------------------------------------------------------------")
a = float(input("Ingrese el valor de a, es el termino al lado del termino de segundo grado: "))
b = float(input("Ingrese el valor de b, es el termino al lado del termino lineal: "))
c = float(input("Ingrese el valor de c, es el termino independiente: "))

# Calculo de datos
print("-----------------------------------------------------------------------------")
d = np.lib.scimath.sqrt((b)**2 - 4 * a * c) #np.lib.scimath.sqrt soporta negativos
x1 = (-b + d) /(2 * a)
x2 = (-b - d) /(2 * a)

# Impresión de datos
print("-----------------------------------------------------------------------------")
print (f"x1 = {x1} | x2 = {x2}")