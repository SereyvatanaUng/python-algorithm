def solve(n, s):
    odd = []
    even = []
    for i in range(0, n):
        if s[i] % 2 == 0:
            odd.append(s[i])
        else:
            even.append(s[i])

    odd.sort()
    even.sort(reverse=True)

    print(" ".join(map(str, odd)))
    print(" ".join(map(str, even)))


N = int(input())
S = list(map(int, input().split()))
solve(N, S)
