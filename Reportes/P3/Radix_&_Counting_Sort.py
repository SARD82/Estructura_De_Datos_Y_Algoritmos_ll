def count_sort(A):
    # Encontrar el elemento máximo del arreglo de entrada.
    M = max(A)


    # Inicializar el arreglo de conteo con 0
    C = [0] * (M + 1)


    # Mapear cada elemento del arreglo de entrada como un índice en el arreglo de conteo
    for num in A:
        C[num] += 1


    # Calcular la suma acumulada en cada índice del arreglo de conteo
    for i in range(1, M + 1):
        C[i] = C[i - 1]


    # Crear el arreglo de salida a partir del arreglo de conteo
    B = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B


# Arreglo de entrada
A = [2, 5, 3, 0, 2, 3, 0, 3]


# Arreglo de salida
B = count_sort(A)


for num in B:
    print(num, end=" ")
# Programa en Python para la implementación de Radix Sort
# Una función para hacer el counting sort del arreglo arr[] según el dígito representado por exp.


def countingSort(A, exp1):


    n = len(A)


    # Los elementos del arreglo de salida que tendrán el arreglo ordenado
    B = [0] * (n)


    # Inicializar el arreglo de conteo con 0
    C = [0] * (10)


    # Almacenar el conteo de ocurrencias en count[]
    for i in range(0, n):
        index = (A[i] / exp1)
        C[int(index % 10)] += 1


    # Cambiar count[i] para que count[i] ahora contenga la posición actual de este dígito en el arreglo de salida
    for i in range(1, 10):
        C[i] += C[i - 1]


    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = (A[i] / exp1)
        B[C[int(index % 10)] - 1] = A[i]
        C[int(index % 10)] -= 1
        i -= 1


    # Copiar el arreglo de salida a arr[], para que arr ahora contenga los números ordenados
    for i in range(0, len(A)):
        A[i] = B[i]


# Método para hacer Radix Sort
def radixSort(A):


    # Encontrar el número máximo para saber cuántos dígitos tiene
    max1 = max(A)


    # Hacer counting sort para cada dígito. Nota que en lugar de pasar el número de dígito, se pasa exp.
    # exp es 10^i donde i es el número del dígito actual
    exp = 1
    while max1 / exp > 0:
        countingSort(A, exp)
        exp *= 10


# Código principal
A = [170, 45, 75, 90, 802, 24, 2, 66]


# Llamada a la función
radixSort(A)


for i in range(len(A)):
    print(A[i])