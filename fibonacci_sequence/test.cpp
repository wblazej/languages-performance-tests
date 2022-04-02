#include <iostream>
#include <time.h>

int fibonacci_sequence(int n) {
    if (n > 1)
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2);
    else
        return n;
}

void test() {
    fibonacci_sequence(30);
}

int main() {
    clock_t start = clock();
    
    test();

    std::cout << (double)(clock() - start) / CLOCKS_PER_SEC * 1000 << std::endl;

    return 0;
}