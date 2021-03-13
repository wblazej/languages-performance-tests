from datetime import datetime
from random import randint

def ts():
    return datetime.now().timestamp()

def execution_time(start: datetime.timestamp, end: datetime.timestamp) -> None:
    print(f"{round((end - start) * 1000, 3)} ms")

if __name__ == "__main__":
    start = ts()

    numbers = [randint(1, 10**6) for _ in range(10**6)]

    end = ts()
    execution_time(start, end)