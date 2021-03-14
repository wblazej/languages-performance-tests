#include <iostream>
#include <time.h>

long factorial(long n) {
    if (n < 0)
        return -1;
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

int main() {
    clock_t start = clock();

    for (int i = 0; i < 100000; i++)
        factorial((long)25);

    clock_t end = clock();

    std::cout << (double)(end - start) / CLOCKS_PER_SEC * 1000 << " ms" << std::endl;

    return 0;
}