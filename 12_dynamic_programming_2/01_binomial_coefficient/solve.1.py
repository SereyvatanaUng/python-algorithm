import sys
sys.setrecursionlimit(10**6)


def solve(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return (solve(n-1, k) + solve(n-1, k-1)) % 10007


N, K = map(int, input().split())
print(solve(N, K))
