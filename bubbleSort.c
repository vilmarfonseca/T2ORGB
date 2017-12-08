
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>
#define tamanho 1000




void bubble_sort(int vetor[], int n) {
   int k, j, aux;
   for (k = 0; k < n - 1; k++) {
      //printf("\n[%d] ", k);
      for (j = 0; j < n - k - 1; j++) {
         //printf("%d, ", j);
         if (vetor[j] > vetor[j + 1]) {
            aux          = vetor[j];
            vetor[j]     = vetor[j + 1];
            vetor[j + 1] = aux;
         }
      }
   }
}


//
// Main
//

void dinamico(){

    int i, seed = 24, *ptr;
    ptr = (int*) calloc(tamanho, sizeof(int));
    if(ptr == NULL)
    {
        printf("Error! memory not allocated.");
        exit(0);
    }

    srand((unsigned) seed);
    for(i = 0 ; i < tamanho ; i++ ) {
        *(ptr + i) = rand() % 999;
    }
    bubble_sort(ptr, tamanho);
    //
   // Mostrar o vetor
   //
   printf("\n{");
   for (i = 0; i < tamanho; i++) {
      printf("%d, ", *(ptr + i));
   }
   printf("}\n");
   free(ptr);
    return;
}

void naodinamico(){

    int i, seed = 24,  vetor[tamanho];


    srand((unsigned) seed);
    for(i = 0 ; i < tamanho ; i++ ) {
        vetor[i] = rand() % 30000;
    }
    bubble_sort(vetor, tamanho);
    //
   // Mostrar o vetor
   //
   printf("\n{");
   for (i = 0; i < tamanho; i++) {
      printf("%d, ", vetor[i]);
   }
   printf("}\n");
   return;
}

int main() {



    naodinamico();

   return;
}

