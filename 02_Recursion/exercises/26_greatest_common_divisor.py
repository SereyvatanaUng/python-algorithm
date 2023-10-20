def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n


N, M = 3, 6
x = gcd(N, M)
for _ in range(x):
    print(1, end='')
