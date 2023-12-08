F = {0: 0, 1: 1}


def fib4(n):
    if n not in F:
        F[n] = (fib4(n-1) + fib4(n-2)) % 10007
    return F[n]


def solve(n, a):
    for i in range(n):
        print(f"F[{a[i]}] = {fib4(a[i])}")


N = int(input())
A = [int(input()) for _ in range(N)]
solve(N, A)
