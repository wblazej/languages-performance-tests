#include <stdio.h>
#include <time.h>

int factorial(int n) {
    if (n == 0)
        return 1;
    
    return n * factorial(n - 1);
}

void test() {
    for (int j = 0; j < 10000; j++)
        for (int i = 1; i <= 20; i++)
            factorial(i);
}

int main() {
    clock_t begin = clock();
    
    test();

    double time_spent = ((double)(clock() - begin) / CLOCKS_PER_SEC) * 1000;
    printf("%f", time_spent);
   
   return 0;
}