def binsearch(low, high, x, S):
    if low > high:  # empty search range
        return -1  # terminate the function
    else:
        # Calculate the middle index mid of the current search range.
        mid = (low + high) // 2
        if x == S[mid]:  # desired element found
            return mid
        elif x < S[mid]:  # search the left half
            return binsearch(low, mid - 1, x, S)
        else:  # x > S[mid] search the right half
            return binsearch(mid + 1, high, x, S)


def solve(n, m, S, X):
    for i in range(m):
        j = binsearch(0, n - 1, X[i], S)
        print(j, end=" ")
    print()


N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)
