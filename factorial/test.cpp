#include <iostream>
#include <time.h>

long long factorial(long n) {
    if (n < 0)
        return -1;
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

void test() {
    for (int i = 0; i < 10000; i++)
        for (int j = 1; j <= 20; j++)
            factorial(j);
}

int main() {
    clock_t start = clock();
    
    test();

    std::cout << (double)(clock() - start) / CLOCKS_PER_SEC * 1000 << std::endl;

    return 0;
}