import time
import math


def solve(n, k):
    return math.comb(n, k) % 10007


N, K = map(int, input().split())
start = time.time()
print(solve(N, K))
end = time.time()
print(f"solve() elapsed time: {end - start}")
