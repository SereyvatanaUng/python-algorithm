def solve(low, high, s):
    pivot = s[low]
    i = low
    for j in range(low + 1, high + 1):
        if s[j] < pivot:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[low], s[i] = s[i], s[low]
    return i


N, L, H = map(int, input().split())
S = list(map(int, input().split()))
pivotpos = solve(L, H, S)
print(pivotpos)
print(*S)
