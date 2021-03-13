from datetime import datetime

def ts():
    return datetime.now().timestamp()

def execution_time(start: datetime.timestamp, end: datetime.timestamp) -> None:
    print(f"{round((end - start) * 1000, 3)} ms")

if __name__ == "__main__":
    start = ts()
    end = ts()
    execution_time(start, end)