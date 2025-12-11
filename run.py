from climb_paths import count_ways
from combine import combine_lists
from filter_dict import filter_young
from logger import log_time
from shapes import main
from upper_decorator import uppercase
from garden import max_flowers



grid = [[1, 0, 1],
        [0, 0, 0],
        [0, 1, 0]]

@uppercase
def greet():
    return "hello student"

@log_time
def hello():
    print("Python is fun!")

print(greet())
hello()

print(max_flowers(grid))