def palindrome(n):
    s = str(n)
    r = s[::-1]
    return n == int(r)


def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        if palindrome(i):
            print(i, end=' ')
            cnt += 1
    print()
    return cnt


N, M = map(int, input().split())
print(N, M)
print(solve(N, M))
