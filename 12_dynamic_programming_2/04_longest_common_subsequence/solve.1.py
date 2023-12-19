def solve(x, y):
    n, m = len(x), len(y)
    dp = [[0]*(m+1) for _ in range(n+1)]
    path = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                path[i][j] = 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                path[i][j] = 2 if dp[i-1][j] > dp[i][j-1] else 3
    return dp[n][m], path


def lcs(i, j, p, x):
    if p[i][j] == 0:
        return ""
    else:
        if p[i][j] == 1:
            return lcs(i-1, j-1, p, x) + x[i-1]
        elif p[i][j] == 2:
            return lcs(i-1, j, p, x)
        elif p[i][j] == 3:
            return lcs(i, j-1, p, x)


X = input()
Y = input()
opt, path = solve(X, Y)
print(opt)
if opt != 0:
    print(lcs(len(X), len(Y), path, X))
