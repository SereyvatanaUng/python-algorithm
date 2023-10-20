# Sample Input 1
# 6
# Sample Output 1
# 6!=(1*2*3*4*5*6)=720

def fact(n):
    if n == 0:
        return 1
    else:
        global i, N
        i += 1
        if i < N:
            print(f"{i}*", end='')
        else:
            print(f"{i})=", end='')
        return n * fact(n - 1)


N = int(input())
i = 0
print(f"{N}!=(", end='')
print(fact(N))
