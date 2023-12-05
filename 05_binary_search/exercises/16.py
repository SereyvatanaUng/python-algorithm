def binsearch(x, n, S):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid - 1
        else:  # x > S[mid]
            low = mid + 1
    return -1


def solve(S, x):
    print(binsearch(x, len(S), S))


S = list(map(int, input().split()))
X = int(input())
solve(S, X)
