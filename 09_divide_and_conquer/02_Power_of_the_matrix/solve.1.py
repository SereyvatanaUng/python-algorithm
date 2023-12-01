def solve(n, A, b):
    C = [A[i] for i in range(n)]
    for _ in range(b - 1):
        C = mmult(n, C, A)
    for i in range(n):
        print(*C[i])


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
solve(N, A, B)
