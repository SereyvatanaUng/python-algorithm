# Sample Input 1
# 3
# Sample Output 1
# 16

def hailstone(n):
    global a
    if n == 1:
        return 1

    if n % 2 == 0:
        result = n // 2
        a.append(result)
        return hailstone(result)

    else:
        result = n * 3 + 1
        a.append(result)
        return hailstone(result)


a = []
N = int(input())
hailstone(N)
print(max(a))
