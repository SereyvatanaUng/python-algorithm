# sample input 1
# 20
# sample output 1
# 42


def sum_div(n):
    s = 0
    sqrtn = int(n ** 0.5)
    for i in range(1, sqrtn + 1):
        if n % i == 0:
            s += (i + n // i)
    return s


N = int(input('Enter a number: '))
print('Sum of divisors:', sum_div(N))
