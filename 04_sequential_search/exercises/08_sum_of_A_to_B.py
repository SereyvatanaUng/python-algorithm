N, M = map(int, input().split())

sum = 0
start = N

while (start-9) % 10 != 0:
    start += 1


for i in range(start, M + 1, 10):
    sum += i
print(sum)
