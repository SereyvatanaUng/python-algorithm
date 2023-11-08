N = list(map(int, input().split()))

for i in range(len(N)):
    s = str(N[i])
    r = s[::-1]
    N[i] = int(r)

print(max(N))
