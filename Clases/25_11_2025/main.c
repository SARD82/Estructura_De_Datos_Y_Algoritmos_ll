#include <stdio.h>
#include <stdlib.h>
#include <time.h> // Se usa time.h para la versión serial

// Definimos el tamaño de los vectores. Debe ser el mismo que el paralelo
#define N 10000000 

int main() {
    // 1. Declaración de variables
    int *A, *B, *C;
    int i;
    clock_t start_time, end_time; // Variables para medir el tiempo

    // 2. Asignación de memoria dinámica
    A = (int*)malloc(N * sizeof(int));
    B = (int*)malloc(N * sizeof(int));
    C = (int*)malloc(N * sizeof(int));

    // Verificar asignación de memoria
    if (A == NULL || B == NULL || C == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        return 1;
    }

    // 3. Inicialización de los vectores A y B
    for (i = 0; i < N; i++) {
        A[i] = i;
        B[i] = N - i;
    }
    
    // --- INICIO DE LA REGIÓN CRÍTICA (Serial) ---

    // Capturamos el tiempo de inicio
    start_time = clock();

    // El bucle 'for' se ejecuta de manera secuencial (por un solo hilo/proceso)
    for (i = 0; i < N; i++) {
        C[i] = A[i] + B[i];
    }
    
    // Capturamos el tiempo de finalización
    end_time = clock();

    // --- FIN DE LA REGIÓN CRÍTICA ---
    
    // 4. Verificación y resultados
    // Calculamos el tiempo en segundos: (final - inicio) / CLOCKS_PER_SEC
    double cpu_time_used = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;

    printf("--- Suma de Vectores Secuencial ---\n");
    printf("Tamaño del vector (N): %d\n", N);
    printf("Tiempo de ejecución secuencial: %.4f segundos\n", cpu_time_used);
    printf("----------------------------------\n");
    printf("Verificación de resultados (Primeros elementos):\n");
    for (i = 0; i < 5; i++) {
        printf("C[%d] = %d\n", i, C[i]);
    }
    printf("...\n");
    printf("Verificación de resultados (Últimos elementos):\n");
    for (i = N - 5; i < N; i++) {
        printf("C[%d] = %d\n", i, C[i]);
    }

    // 5. Liberación de memoria
    free(A);
    free(B);
    free(C);

    return 0;
}
