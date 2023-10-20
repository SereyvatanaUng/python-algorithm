def loop(n):
    # [print(i) for i in range(1, n + 1)]
    print('\n'.join(map(str, range(1, n + 1))))


N = int(input())
loop(N)
