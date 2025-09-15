import matplotlib.pyplot as plt 
import numpy as np

# Datos de cada algoritmo (X = cantidad de elementos, Y = tiempo de ejecución en segundos)
datos_x = [500, 1000, 2000, 5000, 10000, 20000, 40000, 80000, 100000, 150000, 200000, 250000, 300000, 500000, 1000000, 2000000, 3000000, 4000000]

# Tiempos de ejecución
CountingSort = [
    0.0, 0.001009, 0.001000, 0.002005, 0.002005, 0.004005, 0.008, 0.016998,
    0.022999, 0.031999, 0.040516, 0.06652, .118035, .219035, .456218,
    .671463, .910180
]
RadixSort = [
    0.0, 0.000506, 0.000999, 0.004504, 0.009001, 0.020001, 0.040514, 0.086516,
    0.108512, .171796, 0.238034, 0.330546, .741498, 1.608361, 3.295115,
    5.025505, 6.693655
]

# Crear subgráficos
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Quick Sort
datos_qs = np.array([datos_x[:len(CountingSort)], CountingSort]).T
axs[0].plot(datos_qs[:, 0], datos_qs[:, 1], marker='o', linestyle='-', color='red', label="Counting Sort")
axs[0].set_xscale("log")
axs[0].set_yscale("log")
axs[0].set_xlabel("Cantidad de elementos")
axs[0].set_ylabel("Tiempo de ejecución (s)")
axs[0].set_title("Counting Sort")
axs[0].grid(True, linestyle="--", alpha=0.5)
axs[0].legend()

# Heap Sort
datos_hs = np.array([datos_x[:len(RadixSort)], RadixSort]).T
axs[1].plot(datos_hs[:, 0], datos_hs[:, 1], marker='o', linestyle='-', color='blue', label="Radix Sort")
axs[1].set_xscale("log")
axs[1].set_yscale("log")
axs[1].set_xlabel("Cantidad de elementos")
axs[1].set_ylabel("Tiempo de ejecución (s)")
axs[1].set_title("Radix Sort")
axs[1].grid(True, linestyle="--", alpha=0.5)
axs[1].legend()

# Ajustar el espacio entre subgráficos
plt.tight_layout()
plt.show()
