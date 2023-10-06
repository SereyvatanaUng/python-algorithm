# sample input 1
# 1234567
# sample output
# 580763573142020329536784


def odd_pyramid(n):
    return (n * (n + 1) // 2) ** 2


N = int(input())
print(odd_pyramid(N))
