#include <iostream>
#include <time.h>

int main() {
    clock_t tStart = clock();

    for (int i = 0; i < 1000000000; i++) {
        //pass
    }

    std::cout << "Time taken: " << (double)(clock() - tStart)/CLOCKS_PER_SEC * 1000 << "ms" << std::endl;

    return 0;
}