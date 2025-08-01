import time
import threading

def worker(first_await_time):
    print(f"Worker started, will wait for {first_await_time} seconds.")
    time.sleep(first_await_time)

def main():
    start_time = time.perf_counter()
    print("Starting workers...")
    thread_list = []
    for i in range(50):
        t1 = threading.Thread(target=worker, args=(i,))
        thread_list.append(t1)
        t1.start()

    for t in thread_list:
        t.join()
    print("All workers have completed.")
    end_time = time.perf_counter()
    print(f"All workers finished in {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()