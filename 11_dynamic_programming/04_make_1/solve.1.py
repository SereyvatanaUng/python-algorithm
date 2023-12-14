import sys
sys.setrecursionlimit(10**6)


def solve(n):
    if n == 1:
        return 0
    else:
        m = 1 + solve(n-1)
        if n % 3 == 0:
            m = min(m, 1 + solve(n//3))
        if n % 2 == 0:
            m = min(m, 1 + solve(n//2))
        return m


N = int(input())
print(solve(N))
