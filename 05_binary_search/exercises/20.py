def binsearch(x, n, S):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return True
        elif x < S[mid]:
            high = mid - 1
        else:  # x > S[mid]
            low = mid + 1
    return


def solve(A, N):
    for i in range(len(A)):
        if binsearch(N, len(A[i]), A[i]):
            print(True)
            break


A = [list(map(int, input().split())) for _ in range(5)]
N = int(input())

solve(A, N)
