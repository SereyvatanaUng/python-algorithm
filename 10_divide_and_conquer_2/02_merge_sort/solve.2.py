def merge(low, mid, high, s):
    merge.cnt += 1
    c = [0] * (high - low + 1)
    i = low
    j = mid + 1
    k = 0
    while i <= mid and j <= high:
        if s[i] < s[j]:
            c[k] = s[i]
            i += 1
            k += 1
        else:
            c[k] = s[j]
            j += 1
            k += 1
    while i <= mid:
        c[k] = s[i]
        i += 1
        k += 1
    while j <= high:
        c[k] = s[j]
        j += 1
        k += 1
    for k in range(low, high + 1):
        s[k] = c[k-low]


def mergesort(low, high, s):
    if low < high:
        mid = (low + high) // 2
        mergesort(low, mid, s)
        mergesort(mid + 1, high, s)
        merge(low, mid, high, s)


def solve(n, s):
    merge.cnt = 0
    mergesort(0, n - 1, s)
    print(merge.cnt)
    print(*s)


N = int(input())
S = list(map(int, input().split()))
solve(N, S)
