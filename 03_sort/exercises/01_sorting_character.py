def sort_ch(n, s):
    up, low = [], []
    for i in range(n):
        if s[i].isupper():
            up.append(s[i])
        else:
            low.append(s[i])
    return "".join(up), "".join(sorted(low, reverse=True))


x = input().split()
N, S = int(x[0]), x[1]
upper, lower = sort_ch(N, S)
print(upper + "  " + lower)
