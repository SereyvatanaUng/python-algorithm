def euclidean(n, m):
    if n % m == 0:
        return m
    return euclidean(m, n % m)


N, M = map(int, input().split(' '))
print(euclidean(N, M))
