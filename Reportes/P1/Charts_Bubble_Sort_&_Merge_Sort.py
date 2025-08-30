import random, time
import matplotlib.pyplot as plt

# Data generator
def rand_vector(n, low = -1000, high = 1000):
    A = [random.randint(-1000, 1000) for _ in range(n)]
    # Garintize one negative & one positive
    if all(x >= 0 for x in A): -abs(A[0] or 1)
    if all(x <= 0 for x in A): abs(A[1] or 1)
    return A

# Mesuare time
def time_sort(sort_fn, arr):
    B = arr[:]
    t0 = time.perf_counter()
    sort_fn(B)
    t1 = time.perf_counter()
    return t1 - t0

# Bubble & Merge Sort
def bubblesort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        mergesort(L); mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1

# Arrays data
sizes_merge = [500, 1000, 2000, 5000, 10_000, 20_000, 50_000, 100_000, 200_000, 300_000]
sizes_bubble = [500, 1000, 2000, 5000] # I don´t add more data because the complexity of the bubble is O(n^2), wich delays the programs.

results = []

for n in sizes_bubble:
    A = rand_vector(n)
    tb = time_sort(bubblesort, A)
    results.append({"algoritmo":"Bubble", "n":n, "tiempo_s":tb})

for n in sizes_merge:
    A = rand_vector(n)
    tm = time_sort(mergesort, A)
    results.append({"algoritmo":"Merge", "n":n, "tiempo_s":tm})

# Table
print("algoritmo\tn\ttiempo_s")
for r in results:
    print(f"{r['algoritmo']}\t{r['n']}\t{r['tiempo_s']:.6f}")

# Chart
bubble = sorted([r for r in results if r["algoritmo"] == "Bubble"], key = lambda x:x["n"])
merge = sorted([r for r in results if r["algoritmo"] == "Merge"], key = lambda x:x["n"])

plt.figure()
plt.plot([r["n"] for r in bubble], [r["tiempo_s"] for r in bubble], marker = 'o', label = "Bubble sort")
plt.plot([r["n"] for r in merge], [r["tiempo_s"] for r in merge], marker = 'o', label = "Merge Sort")
plt.xlabel("n (cantidad de elementos)")
plt.ylabel("tiempo (segundos)")
plt.title("Relación n vs tiempo")
plt.legend(); plt.grid(True)
plt.show()