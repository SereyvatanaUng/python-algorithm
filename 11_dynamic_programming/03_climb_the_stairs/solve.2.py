def solve(n, a):
    dp = [0] * (n + 1)
    dp[1] = a[1]
    for i in range(2, n+1):
        dp[i] = a[i] + max(dp[i-1], dp[i-2])
    return dp[n]


N = int(input())
A = [0] + list(map(int, input().split()))
print(solve(N, A))
