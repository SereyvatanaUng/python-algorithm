import random
SEED, MIN, MAX, N = 2022, 10, 30, 10
random.seed(SEED)
S = sorted(random.sample(range(MIN, MAX), N))
X = random.sample(range(MIN, MAX), N)
print(f"S ={S}")
print(f"X ={X}")


def binsearch(x, n, S):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return 1
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 0


def solve(N, S, X):
    cnt = 0
    for i in range(N):
        cnt += binsearch(X[i], N, S)
    return cnt


print(solve(N, S, X))
