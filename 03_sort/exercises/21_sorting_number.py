def bubblesort(n, s):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    print('\n'.join(map(str, s)))


N = int(input())
S = [int(input()) for _ in range(N)]
bubblesort(N, S)
