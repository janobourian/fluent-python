import threading
import time
import urllib.request

def get_request(url:str) -> None:
    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", "")
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))

def main() -> None:
    start_time = time.perf_counter()
    total_requests = 500
    threads_list = []
    
    for _ in range(total_requests):
        t = threading.Thread(target=get_request, args=("http://127.0.0.1:8000/api/health",))
        t.start()
        threads_list.append(t)
    
    for i in range(len(threads_list)):
        threads_list[i].join()
        
    print(f"Total time: {time.perf_counter() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()