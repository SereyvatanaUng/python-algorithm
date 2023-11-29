N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
cards = 0
temp = 0
for i in range(0, len(S), 2):
    if i == 0:
        temp += (S[i] + S[i + 1])
        cards += temp
    else:
        cards += (S[i]+temp)
print(cards)
