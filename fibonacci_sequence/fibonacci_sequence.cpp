#include <iostream>
#include <time.h>

int fibonacci_sequence(int n) {
    if (n < 0)
        return -1;
    if (n > 1)
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2);
    else
        return n;
}

int main() {
    clock_t start = clock();

    fibonacci_sequence(30);

    clock_t end = clock();

    std::cout << (double)(end - start) / CLOCKS_PER_SEC * 1000 << " ms" << std::endl;

    return 0;
}