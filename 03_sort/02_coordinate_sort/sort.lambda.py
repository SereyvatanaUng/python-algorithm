S = [(3, 5), (2, 1), (5, 3), (1, 4), (4, 2)]

print(sorted(S, key=lambda k: k[0]))
print(sorted(S, key=lambda k: k[1]))

print('#' * 20)

S = [(2, 5), (2, 1), (1, 3), (1, 4), (1, 2)]
print(sorted(S, key=lambda k: (k[0], k[1])))
print(sorted(S, key=lambda k: (k[0], -k[1])))

S.sort(key=lambda k: (k[0], -k[1]))
print(S)
