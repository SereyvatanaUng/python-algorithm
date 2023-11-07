def binsearch(n, s):
    low, high = 0, n - 1
    mid = (low + high) // 2

    while mid != 0 and mid != (n - 1):
        mid = (low + high) // 2
        if s[mid - 1] < s[mid] > s[mid + 1]:
            return mid

        elif s[mid - 1] < s[mid] < s[mid + 1]:
            low = mid + 1  # right half search

        else:  # s[mid - 1] > s[mid] > s[mid + 1]
            high = mid - 1  # left half search

    return -1  # local maximum not found


def solve(n, s):
    j = binsearch(n, s)
    print(j, s[j])


N = int(input())
S = list(map(int, input().split()))
solve(N, S)
