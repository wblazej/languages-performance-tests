from random import randint
from time import time

def test():
    n = 10 ** 6
    return [randint(1, n) for _ in range(n)]

if __name__ == "__main__":
    start = time()

    test()

    print(round((time() - start) * 1000, 3))