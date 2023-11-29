N = int(input())
S = list(map(int, input().split()))
S.sort()
time = 0
for i in range(len(S)):
    for j in range(i+1):
        time += S[j]
print(time)
