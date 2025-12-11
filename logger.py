import functools
import time

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)
    return wrapper