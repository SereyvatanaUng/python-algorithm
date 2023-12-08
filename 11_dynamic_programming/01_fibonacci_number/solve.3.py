F = [0, 1]


def fib3(n):
    if n < len(F):
        return F[n]
    else:
        for _ in range(len(F), n+1):
            F.append((F[-1] + F[-2]) % 10007)
        return F[n]


def solve(n, a):
    for i in range(n):
        print(f"F[{a[i]}] = {fib3(a[i])}")


N = int(input())
A = [int(input()) for _ in range(N)]
solve(N, A)
