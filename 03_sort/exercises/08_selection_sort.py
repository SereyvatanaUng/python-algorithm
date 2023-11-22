def selectionsort(s):
    cnt = 0
    n = len(s)
    for i in range(n - 1):
        minv, minj = s[i], i
        for j in range(i + 1, n):
            if s[j] > minv:
                minv, minj = s[j], j
        if i != minj:
            s[i], s[minj] = s[minj], s[i]
            cnt += 1
    return s


S = list(map(int, input().split()))
print(selectionsort(S))
