#include <iostream>
#include <time.h>
#include <vector>

int main() {
    clock_t start = clock();

    int n = 1000000;
    std::vector<int> arr;

    for (int i = 0; i < n; i++)
        arr.push_back(rand() % n + 1);

    clock_t end = clock();

    std::cout << (double)(end - start) / CLOCKS_PER_SEC * 1000 << " ms" << std::endl;

    return 0;
}