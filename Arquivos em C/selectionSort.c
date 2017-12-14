#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>

void selectionSort(int vetor[], int tamanho )
{
    int i, iBusca, iMenor;
    int aux;

    for( i = 0; i < tamanho - 1; i++ )
    {
        iMenor = i; // Assume que o menor � o atual

        // Faz a busca por um n�mero menor que o atual, a direita
        for( iBusca = i + 1; iBusca < tamanho; iBusca++ )
        {
            if( vetor[iBusca] < vetor[iMenor] )
            {
                iMenor = iBusca;
            }
        }

        // Se encontrou algum n�mero menor, troca
        if( i != iMenor )
        {
            aux = vetor[i];
            vetor[i] = vetor[iMenor];
            vetor[iMenor] = aux;
        }
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
        *(ptr + i) = rand() % 15000;
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

    selectionSort(ptr, tamanho);

    mostrar_vetor(ptr, tamanho);

    free(ptr);

}
