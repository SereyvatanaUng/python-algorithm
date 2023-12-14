import sys
sys.setrecursionlimit(10**6)

dp = {1: 0, 2: 1, 3: 1}


def solve(n):
    if n not in dp:
        dp[n] = 1 + solve(n - 1)
        if n % 3 == 0:
            dp[n] = min(dp[n], 1 + solve(n//3))
        if n % 2 == 0:
            dp[n] = min(dp[n], 1 + solve(n//2))
    return dp[n]


N = int(input())
print(solve(N))
