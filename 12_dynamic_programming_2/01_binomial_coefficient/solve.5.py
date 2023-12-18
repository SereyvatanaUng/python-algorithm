import time


def solve(n, k):
    k = min(k, n-k)
    B = [1] + [0]*k
    for i in range(n+1):
        for j in range(min(i, k), 0, -1):
            B[j] += B[j-1] % 10007
    return B[k] % 10007


N, K = map(int, input().split())
start = time.time()
print(solve(N, K))
end = time.time()
print(f"solve() elapsed time: {end - start}")
