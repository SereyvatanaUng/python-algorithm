S = [(3, 5), (2, 1), (5, 3), (1, 4), (4, 2)]


def second(k):
    return k[1]


print(sorted(S, key=second))

print(sorted(S, key=second, reverse=True))
