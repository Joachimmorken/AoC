import math


# Puzzle 1
def en():
    with open("1.txt", "r") as f:
        res = 0
        for i in f:
            res += math.floor(int(i) / 3)-2 

        print(res)


def to():
    with open("1.txt", "r") as f:
        res = 0
        for i in f:
            res += rec(int(i))
        
        return res


def rec(n):
    res = math.floor(n / 3)-2
    if res <= 0:
        return 0

    return res + rec(res)
