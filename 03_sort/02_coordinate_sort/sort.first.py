S = [(3, 5), (2, 1), (5, 3), (1, 4), (4, 2)]


def first(k):
    return k[0]


print(sorted(S, key=first))

print(sorted(S, key=first, reverse=True))
