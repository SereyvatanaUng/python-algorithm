def solve(i, j, n, t):
    if i == n - 1:
        return t[i][j]
    else:
        return t[i][j] + max(solve(i+1, j, n, t), solve(i+1, j+1, n, t))


N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
print(solve(0, 0, N, T))
