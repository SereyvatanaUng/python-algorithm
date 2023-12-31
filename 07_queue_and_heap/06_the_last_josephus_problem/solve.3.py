import time
import sys
sys.setrecursionlimit(10 ** 7)


def solve(n, k):
    if n == 1:
        return 1
    else:
        return ((solve(n - 1, k) + k - 1) % n) + 1


N, K = map(int, input().split())
start = time.time()
print(solve(N, K))
end = time.time()
print(f"solve() elapsed time: {end - start}")
