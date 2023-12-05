import random

SEED, N = 1000, 15
random.seed(SEED)
S = sorted(random.sample(range(-10*N, 10*N), N))


def binsearch(n, S):
    low, high = 0, n - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] > 0:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return S[result]


print(binsearch(N, S))
