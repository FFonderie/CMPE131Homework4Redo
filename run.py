from logger import log_time


@log_time
def hello():
    print("Python is fun!")


@log_time
def goodbye(word, number):
    print(word)
    print(number)
hello()
goodbye("a word", 42)