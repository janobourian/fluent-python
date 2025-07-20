import threading
import time

class SquareSumWorkers(threading.Thread):
    
    def __init__(self, n, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._n = n
        self.start()
    
    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i * i
        print(f"Sum of squares up to {self._n}: {sum_squares}")
    
    def run(self):
        self._calculate_sum_squares()

class SleepyWorkers(threading.Thread):
    
    def __init__(self, seconds, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._seconds = seconds
        self.start()
    
    def _sleep_few_seconds(self):
        time.sleep(self._seconds)
    
    def run(self):
        self._sleep_few_seconds()

def main():
    
    start_time = time.perf_counter()
    
    current_workers = []
    for _ in range(100):
        maximum_size = 9999999
        worker = SquareSumWorkers(maximum_size, daemon=True)
        current_workers.append(worker)
    
    for worker in current_workers:
        worker.join()
    
    print(f"Total time: {time.perf_counter() - start_time:.2f} seconds")
    
    second_time = time.perf_counter()
    
    current_sleep_workers = []
    for seconds in range(1, 6):
        worker = SleepyWorkers(seconds, daemon=True)
        current_sleep_workers.append(worker)
    
    for worker in current_sleep_workers:
        worker.join()
    
    print(f"Total time for sleeping workers: {time.perf_counter() - second_time:.2f} seconds")

if __name__ == "__main__":
    main()