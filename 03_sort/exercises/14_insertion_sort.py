def insertionsort(s):
    for i in range(1, len(s)):
        j = i - 1
        val = s[i]
        while j >= 0 and s[j] < val:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = val
    return s


S = list(map(int, input().split()))
print(insertionsort(S))
