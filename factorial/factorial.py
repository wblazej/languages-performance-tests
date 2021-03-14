from datetime import datetime
import sys

def ts():
    return datetime.now().timestamp()

def execution_time(start: datetime.timestamp, end: datetime.timestamp) -> None:
    print(f"{round((end - start) * 1000, 3)} ms")

def factorial(n: float):
    if n < 0:
        return None
    return n * factorial(n - 1) if n > 0 else 1

if __name__ == "__main__":
    start = ts()

    for _ in range(10**5):
        factorial(25)

    end = ts()
    execution_time(start, end)