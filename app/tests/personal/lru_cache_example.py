from functools import lru_cache
import time


@lru_cache(maxsize=128)
def fibonacci(n):
    # print("start Sleeping")
    time.sleep(0.05)
    # print("End Sleeping")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
start_time = time.time()
print(fibonacci(10))
print("Total time: ", time.time() - start_time)
# print(fibonacci(10))