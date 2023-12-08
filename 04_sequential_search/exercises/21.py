def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    for i in range(n, 1000000):
        if is_prime(i) and is_palindrome(i):
            return i


N = int(input())
print(solve(N))
