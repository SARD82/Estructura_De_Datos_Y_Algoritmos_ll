def count_sort(A):
    # Finding the maximum element of input_array.
    M = max(A)
    # Initializing count_arry with 0
    C = [0] * (M + 1)
    # Mapping each element of input_array as an index of count_array
    for num in A:
        C[num] += 1
    # Calculating prefix sum at every index of count count_array
    for i in range(1, M + 1):
        C[i] += C[i - 1]
    # Creating output_array from count_array
    B = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B
    # Input array
A = [2, 5, 3, 0, 2, 3, 0, 3]
    # Outpur array
B = count_sort(A)
for num in B:
    print(num, end=" ")