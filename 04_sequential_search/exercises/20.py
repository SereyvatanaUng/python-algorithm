N = list(map(int, input().split()))
S = int(input())
result = []
for i in range(len(N)-1):
    for j in range(i+1, len(N)):
        if N[i] + N[j] == S:
            result.append([i, j])


print(*result)
