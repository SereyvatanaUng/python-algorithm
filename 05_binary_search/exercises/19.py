# N = list(map(int,input().split()))
# M = int(input())
N = [2, 7, 11, 15]
M = 9
result = []

for i in range(len(N)-1):
    for j in range(i, len(N)):
        if N[i] + N[j] == M:
            result.append(i+1)
            result.append(j+1)
            break

print(result)
