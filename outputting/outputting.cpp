#include <iostream>
#include <time.h>

int main() {
    clock_t start = clock();

    for (int i = 0; i < 10000; i++) {
        std::cout << "Hello World!" << std::endl;
    }

    clock_t end = clock();

    std::cout << (double)(end - start) / CLOCKS_PER_SEC * 1000 << " ms" << std::endl;

    return 0;
}