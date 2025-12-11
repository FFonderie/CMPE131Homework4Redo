from logger import log_time


@log_time
def hello():
    print("Python is fun!")


@log_time
def goodbye(word, number):
    print(word)
    print(number)


@log_time
def returnTest():
    print("returning 5")
    return 5
hello()
goodbye("a word", 42)
print(returnTest())