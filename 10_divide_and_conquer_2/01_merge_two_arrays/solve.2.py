def solve(n, m, a, b):
    c = [0] * (n + m)
    i = j = k = 0
    while i < n and j < m:
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1

    # If there are still elements in arrays
    while i < n:
        c[k] = a[i]
        i += 1
        k += 1
    while j < m:
        c[k] = b[j]
        j += 1
        k += 1
    return c


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*solve(N, M, A, B))
