def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


N, M = input().split()

for i in range(int(N), int(M) + 1):
    if prime(i):
        print(i)
