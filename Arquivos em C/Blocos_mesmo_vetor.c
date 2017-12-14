#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>

void funcao1(int *ptr, int seed, int  tamanho){

    int i;

    int j = 0;
    for(i = 0 ; i < tamanho ; i=i+2 ) {
        *(ptr + j) = *(ptr + i) + *(ptr + (i+1));
        j++;
    }

    //free(ptr);
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
    return;
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

    funcao1(ptr, seed, tamanho);

    mostrar_vetor(ptr, tamanho/2);

    free(ptr);

}
