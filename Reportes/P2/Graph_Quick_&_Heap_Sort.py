import matplotlib.pyplot as plt 
import numpy as np

# Datos de cada algoritmo (X = cantidad de elementos, Y = tiempo de ejecución en segundos)
datos_x = [500, 1000, 2000, 5000, 10000, 20000, 40000, 80000, 100000, 150000, 200000, 250000, 300000, 500000, 1000000, 2000000, 3000000, 4000000]

# Tiempos de ejecución extraídos de las tablas
QuickSort = [
    0.005004, 0.011000, 0.024999, 0.066245, 0.163762, 0.384065, 0.961152, 2.380511,
    3.366041, 6.573511, 11.370160, 16.791345, 23.288667, 236.639748, 898.983951,
    1983.811778, 3519.805172
]
HeapSort = [
    0.014995, 0.034513, 0.075514, 0.217021, 0.490582, 1.028146, 2.223380, 4.771286,
    6.249636, 9.649966, 13.173112, 16.839159, 20.542754, 80.065622, 161.906461,
    249.318062, 336.946019
]

# Crear subgráficos
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Quick Sort
datos_qs = np.array([datos_x[:len(QuickSort)], QuickSort]).T
axs[0].plot(datos_qs[:, 0], datos_qs[:, 1], marker='o', linestyle='-', color='red', label="Quick Sort")
axs[0].set_xscale("log")
axs[0].set_yscale("log")
axs[0].set_xlabel("Cantidad de elementos")
axs[0].set_ylabel("Tiempo de ejecución (s)")
axs[0].set_title("Quick Sort")
axs[0].grid(True, linestyle="--", alpha=0.5)
axs[0].legend()

# Heap Sort
datos_hs = np.array([datos_x[:len(HeapSort)], HeapSort]).T
axs[1].plot(datos_hs[:, 0], datos_hs[:, 1], marker='o', linestyle='-', color='blue', label="Heap Sort")
axs[1].set_xscale("log")
axs[1].set_yscale("log")
axs[1].set_xlabel("Cantidad de elementos")
axs[1].set_ylabel("Tiempo de ejecución (s)")
axs[1].set_title("Heap Sort")
axs[1].grid(True, linestyle="--", alpha=0.5)
axs[1].legend()

# Ajustar el espacio entre subgráficos
plt.tight_layout()
plt.show()
