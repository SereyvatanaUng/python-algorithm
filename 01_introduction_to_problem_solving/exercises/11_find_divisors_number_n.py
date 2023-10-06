from math import sqrt


def divisors(n):
    root_n = int(sqrt(n) + 1)
    other_half = []
    for i in range(1, root_n + 1):
        if n % i == 0:
            print(i)
            other_half.append(n // i)

    print('\n'.join(map(str, other_half[::-1])))


N = 211224
divisors(N)
