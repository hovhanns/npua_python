# import threading lib
import threading
import time
from functools import wraps
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def countdown(n):
    while n > 0:
        n -= 1



@timeit
def run_threaded_file_write(n, number_of_threads):
    threads = []
    for i in range(number_of_threads):
        file_name = f'data/file_{i}_{str(n)}.txt'
        t = threading.Thread(target=write_to_file, args=(file_name,n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
def write_to_file(file_name, lines):
    with open(file_name, 'w') as f:
        for line in range(lines):
            f.write(str(line))
            f.write('\n')
    


@timeit
def run_threaded(n, number_of_threads):
    threads = []
    for i in range(number_of_threads):
        t = threading.Thread(target=countdown, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ =="__main__":
    n = 100000000
    for i in range(0, 5):
        run_threaded(n//(2**i), 2**i)
