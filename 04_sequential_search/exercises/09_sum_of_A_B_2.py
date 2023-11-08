N, M = map(int, input().split())

sum = 0
start = N
for i in range(start, M + 1, 100):
    for j in range(i, i + 10):
        sum += j
print(sum)
