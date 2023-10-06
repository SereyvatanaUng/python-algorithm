# sample input 1
# 12
# 710
# 7
# 257
# 319
# sample output 1
# 12 is a composite number.

# 710 is a composite number.

# 7 is prime number.

# 257 is prime number.

# 319 is a composite number.

# def natural(N):
#     for i in N:
#         is_prime = True
#         sqrti = int(i ** 0.5)
#         for j in range(2, sqrti + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break

#         if is_prime == True:
#             print(i, 'is a prime number.\n')
#         else:
#             print(i, 'is a composite number.\n')


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


N = []
for i in range(5):
    N.append(int(input()))


for n in N:
    if prime(n):
        print(f"{n} is prime number.")
    else:
        print(f"{n} is a composite number.")
    print()
