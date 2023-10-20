# Sample Input 1
# 100000
# Sample Output 1
# 7087323

# def triple_fibonacci(N):
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     if N == 3:
#         return 3

#     fn = [0] * (N + 1)
#     fn[1] = 1
#     fn[2] = 2
#     fn[3] = 3

#     for i in range(4, N + 1):
#         fn[i] = (fn[i - 1] + fn[i - 2] + fn[i - 3]) % (2**32 - 1)
#     return fn[N]


# N = int(input())
# result = triple_fibonacci(N)
# print(result)


def triple_fibonacci(n):
    a, b, c = 1, 2, 3
    for _ in range(4, n + 1):
        a, b, c = b, c, (a + b + c) % (2 ** 32 - 1)
    return c


N = int(input())
print(triple_fibonacci(N))
