#include <iostream>
#include <time.h>
#include <vector>

void test() {
    int n = 1000000;
    std::vector<int> arr;

    for (int i = 0; i < n; i++)
        arr.push_back(rand() % n + 1);
}

int main() {
    clock_t start = clock();
    
    test();

    std::cout << (double)(clock() - start) / CLOCKS_PER_SEC * 1000 << std::endl;

    return 0;
}