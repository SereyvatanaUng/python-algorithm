# Sample Input 1
# 10
# Sample Output 1
# 4

# def magic(n):
#     global coin

#     for i in range(1, n + 1):
#         if i == 1 or i == 2:
#             coin[i] = 1
#             continue
#         if i % 2 == 0:
#             coin[i] = coin[i//2]
#         else:
#             coin[i] = coin[i//2] + coin[i//2+1]


# n = int(input())
# coin = [0] * (n + 1)
# magic(n)
# print(max(coin))

def magic(n, coin, i=1):
    if i == n:
        return max(coin)
    if i == 1 or i == 2:
        coin[i] = 1
    elif i % 2 == 0:
        coin[i] = coin[i // 2]
    else:
        coin[i] = coin[i // 2] + coin[i // 2 + 1]
    return magic(n, coin, i + 1)


n = int(input())
coin = [0] * (n + 1)
print(magic(n, coin))
