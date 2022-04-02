#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int* test() {
    srand(time(NULL));
    
    int n = 1000000;
    int *numbers = malloc(sizeof * numbers * n);

    for (int i = 0; i < n; i++) {
        numbers[i] = rand() % 1000000 + 1;
    }

    return numbers;
}

int main() {
    clock_t begin = clock();
    
    test();

    double time_spent = ((double)(clock() - begin) / CLOCKS_PER_SEC) * 1000;
    printf("%f", time_spent);
   
   return 0;
}