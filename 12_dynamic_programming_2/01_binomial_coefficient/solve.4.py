import time


def solve(n, k):
    k = min(k, n-k)
    B = [[0]*(min(i, k)+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = (B[i-1][j] + B[i-1][j-1]) % 10007
    return B[n][k]


N, K = map(int, input().split())
start = time.time()
print(solve(N, K))
end = time.time()
print(f"solve() elapsed time: {end - start}")
