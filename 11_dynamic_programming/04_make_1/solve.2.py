def solve(n):
    dp = [0, 0, 1, 1] + [0] * (n-3)
    for i in range(4, n + 1):
        dp[i] = 1 + dp[i-1]
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i//3])
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i//2])
    return dp[n]


N = int(input())
print(solve(N))
