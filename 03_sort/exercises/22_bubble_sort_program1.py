def cpp(N, A):
    changed = False
    for i in range(1, N + 2):
        changed = False
        for j in range(N - i):
            if (A[j] > A[j + 1]):
                changed = True
                A[j], A[j + 1] = A[j + 1], A[j]
        if not changed:
            print(i)
            break


N = int(input())
A = [int(input()) for _ in range(N)]
cpp(N, A)
