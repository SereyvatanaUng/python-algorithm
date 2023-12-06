def solve(n, m, a, b):
    return sorted(a + b)


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*solve(N, M, A, B))
