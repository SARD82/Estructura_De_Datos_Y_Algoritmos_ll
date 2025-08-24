def bubbleSort(A):
    comparacion = 0

    for i in range(1,len(A)):
        print("PASADA", i)

        for j in range(len(A) - 1):

            comparacion += 1
            print(f"Comparación {comparacion}")
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
            print(A)

A = [5, 4, 3, 2, 1]
bubbleSort(A)
print("\n")
print(A)