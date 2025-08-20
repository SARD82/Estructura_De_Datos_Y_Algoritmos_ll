# Programa que calcule el valor del número (pi), a partir de la siguiente serie de Leibniz: pi = 4 - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + ... El usuario debe indicar cuantos términos debe llevar la serie.

print("Programa que cálcula el valor de pi a través de serie de Leibniz")

# Input de datos
print("-----------------------------------------------------------------------------")
n = int(input("Ingrese cuántos términos debe llevar la serie: "))

# Cálculo de datos
print("-----------------------------------------------------------------------------")
pi, denominador, signo = 0, 1, 1 # Signo es para sumar o restar.

for _ in range(n):
    pi += signo * (4 / denominador)
    denominador += 2
    signo *= -1 # Para alternar el signo

# Impresión
print("-----------------------------------------------------------------------------")
print(f"Valor aproximado de pi con {n} términos: {pi}")