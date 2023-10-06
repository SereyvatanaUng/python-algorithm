# sample input 1
# 2147483647 4294967295
# sample output 1
# 4294967291 4294967279 4294967231 4294967197 4294967189

def find_prime(n, m):
    prime = []

    if m % 2 == 0:
        m -= 1

    for i in range(m, n - 1, -2):
        is_prime = True
        if i < 3:
            i += 1
        sqrtn = int(i ** 0.5)
        for j in range(2, sqrtn + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(i)

        if len(prime) == 5:
            break

    return sorted(prime, reverse=True)


N, M = map(int, input().split(' '))
print(*find_prime(N, M))
