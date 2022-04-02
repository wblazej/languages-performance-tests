from time import time

def fibonacci_sequence(n: int):
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2) if n > 1 else n

def test():
    fibonacci_sequence(30)

if __name__ == "__main__":
    start = time()

    test()

    print(round((time() - start) * 1000, 3))