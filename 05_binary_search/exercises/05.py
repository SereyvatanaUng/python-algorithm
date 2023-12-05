import random

SEED, MIN, MAX, N = 2022, 10, 30, 10
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(s):
    cnt = 0
    for i in s:
        if is_prime(i):
            cnt += 1
    return cnt


print(solve(S))
