# Sample Input 1
# 6
# Sample Output 1
# 720

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


N = int(input())
print(fact(N))
