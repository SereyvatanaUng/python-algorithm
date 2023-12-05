def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n, m):
    summ = 0
    j = []
    for i in range(n, m+1):
        if is_prime(i):
            j.append(i)
            summ += i
    return j, summ


N, M = map(int, input().split())
arr, result = solve(N, M)
print(*arr)
print(result)
