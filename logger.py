def log_time(func):
    import time
    def wrapper():
        print(time.ctime())
        func()
    return wrapper