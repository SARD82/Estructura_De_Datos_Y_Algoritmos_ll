import random

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the ,id of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Checking if any elements was left in L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Checking if any elements was left in R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()

arr = [random.randint(-1000, 1000) for _ in range(10)] #Change the letter "n" for the number of components that u array is gonna have
print("Given array is", end = "\n")
printList(arr)
mergeSort(arr)
print("Sorted array is", end = "\n")
printList(arr)