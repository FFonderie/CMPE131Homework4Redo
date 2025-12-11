def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper