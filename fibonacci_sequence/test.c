#include <stdio.h>
#include <time.h>

int fibonacci_sequence(int n) {
    if (n <= 1)
        return 1;

    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2);
}

void test() {
    fibonacci_sequence(30);
}

int main() {
    clock_t begin = clock();
    
    test();

    double time_spent = ((double)(clock() - begin) / CLOCKS_PER_SEC) * 1000;
    printf("%f", time_spent);
   
   return 0;
}