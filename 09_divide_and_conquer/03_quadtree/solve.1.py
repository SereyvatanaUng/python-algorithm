def quadtree(i, j, n, A):
    chk = check(i, j, n, A)
    if chk < 2:
        return "W" if chk == 0 else "B"
    else:
        m = n // 2
        s1 = quadtree(i, j, m, A)
        s2 = quadtree(i, j+m, m, A)
        s3 = quadtree(i+m, j, m, A)
        s4 = quadtree(i+m, j+m, m, A)
        return "Q" + s1 + s2 + s3 + s4


def check(i, j, n, A):
    for r in range(i, i + n):
        for c in range(j, j + n):
            if A[r][c] != A[i][j]:
                return 2
    return A[i][j]


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(quadtree(0, 0, N, A))
