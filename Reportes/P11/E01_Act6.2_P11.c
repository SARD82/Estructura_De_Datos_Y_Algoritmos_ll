#include <stdio.h>
#include <stdlib.h>
#include <omp.h>  // Incluimos la biblioteca de OpenMP

#define n 10  // Tamaño del arreglo
#define NUM_THREADS 2  // Número de hilos a usar

void llenaArreglo(int *a);
void suma(int *A, int *B, int *C);

int main() {
    int *a, *b, *c;

    // Asignación de memoria
    a = (int *)malloc(sizeof(int) * n);
    b = (int *)malloc(sizeof(int) * n);
    c = (int *)malloc(sizeof(int) * n);

    // Llenar los arreglos
    printf("Arreglo A:\n");
    llenaArreglo(a);
    printf("Arreglo B:\n");
    llenaArreglo(b);

    // Realizar la suma paralela
    suma(a, b, c);

    // Imprimir resultado completo
    printf("\nResultado final C:\n");
    for(int i = 0; i < n; i++) {
        printf("%d\t", c[i]);
    }
    printf("\n");

    // Liberar memoria
    free(a);
    free(b);
    free(c);

    return 0;
}

void llenaArreglo(int *a) {
    for(int i = 0; i < n; i++) {
        a[i] = rand() % n;  // Números entre 0 y 9
        printf("%d\t", a[i]);
    }
    printf("\n");
}

void suma(int *A, int *B, int *C) {
    int i, tid, inicio, fin;
    
    // Configurar número de hilos
    omp_set_num_threads(NUM_THREADS);
    
    // Paralelizar el bucle
    #pragma omp parallel private(inicio, fin, tid, i)
    {
        tid = omp_get_thread_num();  // Obtener ID del hilo
        inicio = tid * (n / NUM_THREADS);  // Cálculo del inicio
        fin = (tid + 1) * (n / NUM_THREADS);  // Cálculo del fin
        
        printf("Hilo %d trabajando desde %d hasta %d\n", tid, inicio, fin-1);
        
        for(i = inicio; i < fin; i++) {
            C[i] = A[i] + B[i];
            printf("Hilo %d calculó C[%d] = %d\n", tid, i, C[i]);
        }
    }
}