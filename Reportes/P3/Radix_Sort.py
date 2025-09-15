# Python program for implementation of Radiz Sort
# A function to do counting sort of arr[] acording to
# the digit represented by exp.

def countingSort(A, exp1):
    
    n = len(A)

    # The output array elements that will have sorted arr
    B = [0] * (n)

    # Initialize count array as 0
    C = [0] * (10)

    # Store count of currences in count[]
    for i in range(0, n):
        index = (A[i] / exp1)
        C[int(index % 10)] = C[int(index % 10)] + 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        C[i] = C[i] + C[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (A[i] / exp1)
        B[C[int(index % 10)] - 1] = A[i]
        C[int(index % 10)] = C[int(index % 10)] - 1
        i -=1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(A)):
            A[i] = B[i]

# Metod to do radix sort
def radixSort(A):

    # finding the maximum number to know number of digits
    max1 = max(A)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(A, exp)
        exp *= 10

# Driver code
A = [170, 45, 75, 90, 802, 24, 2, 66]

# Function call
radixSort(A)

for i in range(len(A)):
    print(A[i])