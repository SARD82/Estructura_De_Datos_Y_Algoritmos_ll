def bubbleSort(A):
    for i in range(len(A) - 1):
        print("PASADA", i)
        for j in range(len(A) - i - 1):

            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
            print(A)

A = [5, -4, 3, -2, 1]
bubbleSort(A)
print("\n")
print(A)