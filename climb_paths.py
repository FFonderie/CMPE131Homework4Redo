def count_ways(n):
    if (n < 1 or n > 30):
        raise ValueError(f"stop that. You cannot climb a " + str(n) + " step stair")

    # make a list of size n+2 (for 1, its 3) with default value 1
    ways = [1] * (n+2) 

    # first instance is all that is needed
    ways[2] = 2
    ways[n+1] = -1 # prevents out of bounds

    for i in range(3,n+1):
        ways[i] = ways[i-3] + ways[i-2] + ways[i-1]
    return ways[n]