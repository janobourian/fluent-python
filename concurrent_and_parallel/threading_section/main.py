import time
import threading

def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i * i
    print(f"Sum of squares up to {n}: {sum_squares}")

def sleep_few_seconds(seconds):
    time.sleep(seconds)


def main():
    calc_start_time = time.time()
    
    current_threads = []
    for i in range(5):
        maximum_size = 9999999
        t = threading.Thread(target=calculate_sum_squares, args=(maximum_size,), daemon=True)
        t.start()
        current_threads.append(t)
    
    for i in range(len(current_threads)):
        current_threads[i].join()

    calc_sum_squares_time = time.time()
    print(f"Time taken to calculate sum of squares: {calc_sum_squares_time - calc_start_time:.2f} seconds")
    print("Calculating sum of squares completed.")
    
    print("Sleeping for a few seconds...")
    current_threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_few_seconds, args=(seconds,), daemon=True)
        t.start()
        # t.join()
        current_threads.append(t)
    
    for i in range(len(current_threads)):
        current_threads[i].join()
        
    calc_end_time = time.time()
    print(f"Time taken to calculate the sleeping process: {calc_end_time - calc_sum_squares_time:.2f} seconds")

if __name__ == "__main__":
    main()