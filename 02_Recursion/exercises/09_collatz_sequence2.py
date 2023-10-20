# Sample Input 1
# 10
# Sample Output 1
# 4

def collatz(n):
    global cnt
    if n == 1:
        return n
    if n % 2 == 0:
        cnt += 1
        return collatz(n // 2)
    else:
        cnt += 1
        return collatz((n + 1) // 2)


N = int(input())
cnt = 0
collatz(N)
print(cnt)
