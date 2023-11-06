def factorize(n, m):
    if n < 2:
        return []
    elif m > int(n ** 0.5):
        return [n]
    elif n % m == 0:
        return [m] + factorize(n // m, m)
    else:
        return factorize(n, m + 1)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        factors = factorize(i, 2)
        if len(factors) > 1:
            cnt += 1
    return cnt


N, M = map(int, input().split())
print(solve(N, M))
