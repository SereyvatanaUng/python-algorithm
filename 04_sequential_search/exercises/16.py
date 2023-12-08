def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(N):
    result = []
    for i in range(3, N):
        if is_prime(i):
            result.append(i)
            fact = 1
            for j in range(i, 0, -1):
                if is_prime(j):
                    fact *= j
                if fact > N:
                    return result
    return result


N = int(input())
print(*solve(N))
