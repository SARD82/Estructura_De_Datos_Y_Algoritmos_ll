import random

def bubbleSort(A):
    for i in range(1,len(A)):
        # Deleting print to optimize
        for j in range(len(A) - 1):

            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
            # Deleting print to optimize

A = [random.randint(-1000, 1000) for _ in range(n)] #Change the letter "n" for the number of components that u array is gonna have
print("Given array\n\n", A)
bubbleSort(A)
print("\n")
print(A)