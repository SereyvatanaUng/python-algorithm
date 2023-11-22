def solve(n, k, a, b):
    for i in range(k):
        a[i], b[n-i-1] = b[n-i-1], a[i]
    return sum(a)


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, K, A, B))
