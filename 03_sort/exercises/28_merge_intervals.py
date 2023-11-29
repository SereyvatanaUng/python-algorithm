# 4
# 1 3
# 2 6
# 8 10
# 15 18

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
intervals = []

for i in range(1, len(S)):
    if S[i-1][1] > S[i][0]:
        intervals.append([S[i-1][0], S[i][1]])
    else:
        intervals.append(S[i])

print(intervals)
