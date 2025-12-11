def log_time(func):
    import time
    def wrapper(*args, **kwargs):
        print(time.ctime())
        func(*args, **kwargs)
    return wrapper