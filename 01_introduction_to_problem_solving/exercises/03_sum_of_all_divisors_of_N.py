# sample input 1
# 1234567890
# sample output 1
# 3211610688


def sum_divisors(n):
    s = 0
    sqrtn = int(n ** 0.5)
    
    for i in range(1, sqrtn + 1):
        if n % i == 0:
            s += (i + n // i)

    return s


N = int(input())
print(sum_divisors(N))