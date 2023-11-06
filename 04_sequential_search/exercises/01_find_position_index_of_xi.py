import random


def search(x, S):
    for i in range(len(S)):
        if x == S[i]:
            return i
    return -1


def solve(S, X):
    for i in range(len(X)):
        print(search(X[i], S), end=" ")
    print()


SEED, MIN, MAX, N = 2022, 10, 30, 10
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)
X = random.sample(range(MIN, MAX), N)
solve(S, X)
