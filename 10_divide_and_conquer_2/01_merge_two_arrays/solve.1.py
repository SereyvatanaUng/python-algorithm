def solve(n, m, a, b):
    c = []
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*solve(N, M, A, B))
