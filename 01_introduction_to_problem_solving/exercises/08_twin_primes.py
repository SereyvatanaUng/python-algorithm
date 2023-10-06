# sample input 1
# 10
# sample output 1
# 3 5
# 5 7
# 2


def prime_prime(n):
    prime = []
    twin = []
    for i in range(1, n + 1):
        is_prime = True
        if i <= 1:
            continue

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False

        if is_prime == True:
            if len(prime) > 0 and i == prime[-1]+2:
                twin.append([prime[-1], i])
            prime.append(i)

    return twin, len(twin)


N = int(input())
twin, pairs = prime_prime(N)

for a, b in twin:
    print(a, b)
print(pairs)
