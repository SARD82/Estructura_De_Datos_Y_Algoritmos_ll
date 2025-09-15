import random  # Para generar números aleatorios
import time  # Para medir tiempos de ejecución


TAM = 500  # Tamaño del arreglo a ordenar


def ordenamiento_por_conteo(A):
    """ Implementación del algoritmo de ordenamiento por conteo que maneja números negativos. """
    if not A:  # Si la lista está vacía, se retorna tal cual.
        return A


    min_val = min(A)  # Obtener el menor valor
    max_val = max(A)  # Obtener el mayor valor
    rango_valores = max_val - min_val + 1  # Rango de valores en el arreglo


    # Crear el arreglo de conteo con el tamaño adecuado
    conteo = [0] * rango_valores  


    # Contar las ocurrencias de cada número
    for num in A:
        conteo[num - min_val] += 1


    # Reconstruir el arreglo ordenado
    resultado = []
    for i in range(rango_valores):
        resultado.extend([i + min_val] * conteo[i])


    return resultado
def ordenamiento_por_digitos(A):
    """ Implementación del algoritmo Radix Sort que maneja números negativos. """
    if not A:
        return A


    # Separar números negativos y positivos
    negativos = [-num for num in A if num < 0]
    positivos = [num for num in A if num >= 0]


    # Determinar el mayor valor absoluto en la lista
    max_val = max(abs(min(A)), max(A))


    # Ordenar positivos
    exp = 1
    while max_val // exp > 0:
        positivos = ordenamiento_auxiliar_radix(positivos, exp)
        exp *= 10


    # Ordenar negativos (se convierten a positivos, se ordenan y luego se revierte el orden)
    exp = 1
    while max_val // exp > 0:
        negativos = ordenamiento_auxiliar_radix(negativos, exp)
        exp *= 10


    negativos = [-num for num in reversed(negativos)]  # Revertimos el orden de los negativos


    return negativos + positivos  # Unimos los negativos y positivos ordenados    
def ordenamiento_auxiliar_radix(A, exp):
    """ Función auxiliar de Radix Sort que ordena los elementos según un dígito específico (exp). """
    n = len(A)
    resultado = [0] * n  # Lista de salida
    conteo = [0] * 10  # Contador para los dígitos (0-9)


    # Contar ocurrencias de los dígitos en la posición actual (exp)
    for num in A:
        indice = abs(num) // exp % 10
        conteo[indice] += 1


    # Convertir conteo[i] en la posición real en la lista resultado
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]


    # Construir el arreglo ordenado
    for num in reversed(A):  # Se recorre al revés para estabilidad
        indice = abs(num) // exp % 10
        resultado[conteo[indice] - 1] = num
        conteo[indice] -= 1


    return resultado


def imprimir_lista(lista):
    """ Imprime una lista en la consola. """
    print(" ".join(map(str, lista)))
# Generar una lista aleatoria de números enteros entre -1000 y 1000
A = [random.randint(-1000, 1000) for _ in range(TAM)]


# Medir tiempo de ejecución de Radix Sort
inicio_radix = time.time()
A_ordenado_radix = ordenamiento_por_digitos(A.copy())  # Se usa copy() para evitar modificar A
fin_radix = time.time()


# Medir tiempo de ejecución de Counting Sort
inicio_counting = time.time()
A_ordenado_conteo = ordenamiento_por_conteo(A.copy())
fin_counting = time.time()


# Mostrar resultados en consola
print("Arreglo ordenado con Counting Sort:")
imprimir_lista(A_ordenado_conteo)


print("\nArreglo ordenado con Radix Sort:")
imprimir_lista(A_ordenado_radix)


# Mostrar tiempos de ejecución
print(f"\nTiempo de ejecución Radix Sort ({TAM} elementos): {fin_radix - inicio_radix:.6f} segundos")
print(f"Tiempo de ejecución Counting Sort ({TAM} elementos): {fin_counting - inicio_counting:.6f} segundos")