#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>

void funcao2(int *ptr, int seed, int  tamanho){

    int i;


    int j = tamanho;
    for(i = 0 ; i < tamanho ; i=i+2 ) {
        *(ptr + j) = *(ptr + i) + *(ptr + (i+1));
        j=j+8;
    }

    // [ 1][ 2][ 3][ 4][ 5][6 ][ 7][ 8][9 ][0 ][ 1][ 2][ 3][ 4][ 5][ 6]   ,    [ 3][ ][ ][ ][ ][ ][ ][7 ][ ][ ][ ][ ][ ][ ][ ][ ]

    //
    // Mostrar o vetor de 8 em 8
    //
    printf("\nVetor ordenado\n");
    j = tamanho;
    for (i = 0; i < tamanho/2; i++) {
        printf("%d, ", *(ptr + j));
        j = j+8;
    }
}



void popular(int *ptr, int tamanho, int seed)
{
    int i;
    if(ptr == NULL)
    {
        printf("Error! memory not allocated.");
        exit(0);
    }

    srand((unsigned) seed);
    for(i = 0 ; i < tamanho ; i++ ) {
        *(ptr + i) = rand() % 50;
    }
}

void mostrar_vetor(int *ptr, int tamanho){
    int i;
    printf("\nVetor\n");
    for (i = 0; i < tamanho; i++) {
      printf("%d, ", *(ptr + i));
    }
}


int main() {
    int *ptr, tamanho = 1000, seed = 24, i;

    ptr = (int*) calloc(tamanho, sizeof(int));

    popular(ptr, tamanho, seed);

    mostrar_vetor(ptr, tamanho);

    funcao2(ptr, seed, tamanho);

    free(ptr);

}
