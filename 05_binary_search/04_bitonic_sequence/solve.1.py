def binsearch(low, high, n, s):
    mid = (low + high) // 2
    if mid == 0 or mid > (n - 1):
        return -1

    else:
        if s[mid - 1] < s[mid] > s[mid + 1]:
            return mid

        elif s[mid - 1] < s[mid] < s[mid + 1]:
            # recursively (search the right half)
            return binsearch(mid + 1, high, n, s)

        else:  # s[mid - 1] > s[mid] > s[mid + 1]
            # recursively (search the left half)
            return binsearch(low, mid - 1, n, s)


def solve(n, s):
    j = binsearch(0, n - 1, n, s)
    print(j, s[j])


N = int(input())
S = list(map(int, input().split()))
solve(N, S)
