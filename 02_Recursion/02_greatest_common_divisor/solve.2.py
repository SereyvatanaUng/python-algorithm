def gcd(n, m):
    while m != 0:
        print(n, m)
        n, m = m, n % m
    return n


N = int(input())
M = int(input())
print(gcd(N, M))
