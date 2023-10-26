def solve(s):
    s.sort()

    # while len(s) > 0:
    while s:
        mid = (len(s) - 1) // 2
        # print(s[mid], end=" ")
        print(s, mid, s[mid])
        s.remove(s[mid])
    print()


N = int(input())
S = list(map(int, input().split()))
solve(S)
