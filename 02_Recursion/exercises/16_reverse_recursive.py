def rev_rec(n):
    if n == 1:
        print(1)
        return
    print(n, end=' ')
    rev_rec(n - 1)


N = int(input())
rev_rec(N)
