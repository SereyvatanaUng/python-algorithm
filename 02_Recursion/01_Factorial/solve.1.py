import sys


def fact(n) :
    if n == 0 :
        return 1
    else :
        return n * fact(n - 1)


sys.setrecursionlimit(10 ** 5)
N = int(input())
print(fact(N))