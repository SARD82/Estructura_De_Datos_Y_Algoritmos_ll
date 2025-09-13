import random
import time
import sys


TAM = 4000000

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def particionar(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def Quicksort(A, p, r):
    if p < r:
        q = particionar(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)

def printListFile(arr, file):
    for i in range(len(arr)):
        print(arr[i], end=" ", file=file)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
sys.setrecursionlimit(3000)  # Ajusta según necesidad
arrayTam = TAM
A = [random.randint(-1000, 1000) for i in range(arrayTam)]
inicioQuick = time.time()
Quicksort(A.copy(), 0, TAM - 1)
finQuick = time.time()

inicioHeap = time.time()
heapSort(A)
finHeap = time.time()
with open("C:/Users/poder/Documentos/pyth/Output/salida2.txt", "a") as f:
    print("Sorted array is: ", file=f)
    printListFile(A, f)
    print(f"\nTiempo de ejecucion QuickSort({arrayTam}): {finQuick - inicioQuick:.6f} segundos", file=f)
    print(f"Tiempo de ejecucion HeapSort({arrayTam}): {finHeap - inicioHeap:.6f} segundos", file=f)
    #f.write(" ".join(map(str, A)) + "\n")
    f.write("="*50 + "\n")  # L�nea divisoria para diferenciar 
print("Sorted array is: ")
printList(A)
print(f"\nTiempo de ejecucion QuickSort({arrayTam}): {finQuick - inicioQuick:.6f} segundos")
print(f"Tiempo de ejecucion HeapSort({arrayTam}): {finHeap - inicioHeap:.6f} segundos")
