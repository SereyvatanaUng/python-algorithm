dp = {1: 1, 2: 2}


def solve(n):
    if n not in dp:
        dp[n] = (solve(n-1) + solve(n-2)) % 10007
    return dp[n]


N = int(input())
print(solve(N))
