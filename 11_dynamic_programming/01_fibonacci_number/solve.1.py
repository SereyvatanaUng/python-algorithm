def fib1(n):
    if n < 2:
        return n
    else:
        return (fib1(n-1) + fib1(n-2)) % 10007


def solve(n, a):
    for i in range(n):
        print(f"F[{a[i]}] = {fib1(a[i])}")


N = int(input())
A = [int(input()) for _ in range(N)]
solve(N, A)
