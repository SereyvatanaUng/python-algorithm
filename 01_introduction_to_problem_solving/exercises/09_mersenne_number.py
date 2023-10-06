# sample input 1
# 10
# sample output 1
# 3
# 7

# sample input 2
# 100
# sample output 2
# 3
# 7
# 31


from math import log2, sqrt


def mersenne(N):
    mersenne_num = []
    n = int(log2(N))
    for i in range(2, n + 1):
        is_prime = True
        sqrti = int(sqrt(2**i - 1))
        num = 2 ** i - 1

        for j in range(2, sqrti + 1):
            if num % j == 0:
                is_prime = False

        if is_prime == True:
            mersenne_num.append(num)

    return mersenne_num


N = int(input())
for i in mersenne(N):
    print(i)
