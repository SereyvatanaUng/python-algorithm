def ackermann(n, m):
    global cnt
    cnt += 1
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return ackermann(n - 1, 1)
    else:
        result = ackermann(n - 1, ackermann(n, m - 1))
    return result


cnt = 0
n, m = map(int, input().split(' '))
print(ackermann(n, m))
print(cnt)
