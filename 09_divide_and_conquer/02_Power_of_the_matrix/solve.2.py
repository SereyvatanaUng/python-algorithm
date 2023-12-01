def solve(n, A, b):
    if b == 1:
        return A
    else:
        C = solve(n, A, b//2)
        if b % 2 == 0:
            return mmult(n, C, C)
        else:
            return mmult(n, A, mmult(n, C, C))


def mmult(n, A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j] % 1000
            C[i][j] %= 1000
    return C


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = solve(N, A, B)
for i in range(N):
    print(*C[i])
