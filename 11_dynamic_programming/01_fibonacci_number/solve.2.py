def fib2(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, (a + b) % 10007
        return b


def solve(n, a):
    for i in range(n):
        print(f"F[{a[i]}] = {fib2(a[i])}")


N = int(input())
A = [int(input()) for _ in range(N)]
solve(N, A)
