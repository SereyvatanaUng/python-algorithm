# sample input 1
# 77 11
# sample output 1
# 266711567621704128000

def perm(n, r):
    if r == 0:
        return 1
    if n < r:
        return 0
    return n * perm(n - 1, r - 1)


n, r = map(int, input().split(' '))
print(perm(n, r))
