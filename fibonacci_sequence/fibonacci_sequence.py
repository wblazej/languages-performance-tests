from datetime import datetime

def ts():
    return datetime.now().timestamp()

def execution_time(start: datetime.timestamp, end: datetime.timestamp) -> None:
    print(f"{round((end - start) * 1000, 3)} ms")

def fibonacci_sequence(n: int):
    if n < 0: 
        return None
    return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2) if n > 1 else n

if __name__ == "__main__":
    start = ts()

    fibonacci_sequence(30)

    end = ts()
    execution_time(start, end)