#include <stdio.h>
#include <omp.h>

int main() {
    #pragma omp parallel
    {
        printf("Hola Mundo\n");

        #pragma omp for
        for (int i = 0; i < 10; i++)
            printf("Iteracion: %d\n", i);
    }

    printf("Adiós\n");
    return 0;
}

