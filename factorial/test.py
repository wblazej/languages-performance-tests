from time import time

def factorial(n: float):
    if n < 0:
        return None
    return n * factorial(n - 1) if n > 0 else 1

def test():
    for _ in range(10 ** 4):
        for i in range(20):
            factorial(i + 1)

if __name__ == "__main__":
    start = time()

    test()

    print(round((time() - start) * 1000, 3))