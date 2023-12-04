import concurrent.futures
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
def pool_thread(max_workes):

    pool = concurrent.futures.ThreadPoolExecutor(max_workers=(2**max_workes))
    n = 100000000

    results = [pool.submit(countdown, n//2**i) for i in range(2**max_workes)]
    pool.shutdown(wait=True)


if __name__ =="__main__":
    n = 100000000
    for i in range(0, 5):
        pool_thread(i)
