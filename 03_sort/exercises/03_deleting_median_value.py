import random


def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)


def median(s, n):
    s.sort()
    i = 1
    index = s[0]
    while i <= n:
        mid = (len(s) - 1) // 2
        index = s[mid]
        s.remove(s[mid])
        i += 1
    return index


# SEED, MIN, MAX, N, K = 2022, 10, 100, 15, 5
SEED, MIN, MAX, N, K = map(int, input().split(" "))
S = generate(SEED, MIN, MAX, N)
print(median(S, K))
