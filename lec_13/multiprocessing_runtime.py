
import multiprocessing

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
def run_process(n, number_of_threads):
    process = []
    for i in range(number_of_threads):
        t = multiprocessing.Process(target=countdown, args=(n,))
        process.append(t)
        t.start()
    for t in process:
        t.join()
    

if __name__ == '__main__':
    n = 100000000
    for i in range(0, 8):
        run_process(n//(2**i), 2**i)

