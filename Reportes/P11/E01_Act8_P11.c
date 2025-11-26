#include <stdio.h>
#include <omp.h>

void suma(int *A, int *B, int *C, int n) {
    int i, tid;
    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        #pragma omp for
        for (i = 0; i < n; i++) {
            C[i] = A[i] + B[i];
            printf("Hilo %d calculo C[%d] = %d\n", tid, i, C[i]);
        }
    }
}

int main() {
    int A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int B[] = {21, 22, 23, 24, 25, 26, 27, 28, 29, 30};
    int C[10];
    int n = 10;

    
    suma(A, B, C, n);

    
    printf("Resultado final (C):\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", C[i]);
    }

    printf("\n");

    return 0;
}
//Ramirez Alvarez Jonathan Gibran
