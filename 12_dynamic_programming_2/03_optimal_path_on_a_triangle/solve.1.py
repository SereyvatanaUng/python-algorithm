def solve(n, t):
    dp = [t[i][:] for i in range(n)]
    path = [[-1]*(i+1) for i in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if dp[i+1][j] >= dp[i+1][j+1]:
                dp[i][j] += dp[i+1][j]
                path[i][j] = 0
            else:
                dp[i][j] += dp[i+1][j+1]
                path[i][j] = 1
    return dp[0][0], path


N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
opt, path = solve(N, T)
print(opt)
j = 0
for i in range(N):
    print(T[i][j], end=" ")
    j += path[i][j]
print()
