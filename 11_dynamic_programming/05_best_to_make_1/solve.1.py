def solve(n):
    dp = [0, 0, 1, 1] + [0] * (n-3)
    path = [0, 0, 1, 1] + [0] * (n-3)
    for i in range(4, n+1):
        dp[i] = 1 + dp[i-1]
        path[i] = i-1
        if i % 2 == 0 and dp[i] >= 1 + dp[i//2]:
            dp[i] = 1 + dp[i//2]
            path[i] = i//2

        if i % 3 == 0 and dp[i] >= 1 + dp[i//3]:
            dp[i] = 1 + dp[i//3]
            path[i] = i//3

    return dp[n], path


N = int(input())
opt, path = solve(N)
print(opt)
print(N, end=" ")
while N > 1:
    print(path[N], end=" ")
    N = path[N]
print()
print(*path)
