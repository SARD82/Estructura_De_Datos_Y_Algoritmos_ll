def busqueda_lineal_recursiva(A, x, ini, fin):
    if ini > fin:
        return -1
    if A[ini] == x:
        return ini
    return busqueda_lineal_recursiva(A, x, ini + 1, fin)

A = [4, 8, 15, 16, 23, 42]
x = 16
resultado = busqueda_lineal_recursiva(A, x, 0, len(A) - 1)
print("Resultado:", resultado)
