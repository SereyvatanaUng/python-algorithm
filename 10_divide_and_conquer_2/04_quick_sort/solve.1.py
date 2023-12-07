def partition(low, high, s):
    partition.cnt += 1
    pivot = s[low]
    i = low
    for j in range(low+1, high+1):
        if s[j] < pivot:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[low], s[i] = s[i], s[low]
    return i


def quicksort(low, high, s):
    if low < high:
        pivotpos = partition(low, high, s)
        quicksort(low, pivotpos-1, s)
        quicksort(pivotpos+1, high, s)


N = int(input())
S = list(map(int, input().split()))
partition.cnt = 0
quicksort(0, N-1, S)
print(partition.cnt)
print(*S)
