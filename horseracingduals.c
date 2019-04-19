#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


int main() {
    int N;
    int diff_min = 10000000;
    scanf("%d", &N);
    int Pi[N], diff[N];
    int former_puissance = 0;

    for (int i = 0; i < N; i++) {
        scanf("%d", &Pi[i]);
    }

    qsort(Pi, N, sizeof(int), cmpfunc);

    for (int i = 0 ; i < N ; i++) {
        diff[i] = (fabs(Pi[i] - former_puissance));
        former_puissance = Pi[i];
    }

    qsort(diff, N, sizeof(int), cmpfunc);

    printf("%d", diff[0]);
    return 0;
}