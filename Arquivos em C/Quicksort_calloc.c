#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>

void quick_sort(int *a, int left, int right) {
    int i, j, x, y;

    i = left;
    j = right;
    x = a[(left + right) / 2];

    while(i <= j) {
        while(a[i] < x && i < right) {
            i++;
        }
        while(a[j] > x && j > left) {
            j--;
        }
        if(i <= j) {
            y = a[i];
            a[i] = a[j];
            a[j] = y;
            i++;
            j--;
        }
    }

    if(j > left) {
        quick_sort(a, left, j);
    }
    if(i < right) {
        quick_sort(a, i, right);
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
    int *ptr, tamanho = 20, seed = 24, i;

    ptr = (int*) calloc(tamanho, sizeof(int));

    popular(ptr, tamanho, seed);

    mostrar_vetor(ptr, tamanho);

    quick_sort(ptr, 0, tamanho - 1);

    mostrar_vetor(ptr, tamanho);

    free(ptr);

}
