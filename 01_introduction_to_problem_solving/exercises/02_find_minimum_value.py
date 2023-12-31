# sample input 1
# 1987 123 4567 89
# sample output 1
# 141 16

import random


def find_min(s):
    small = s[0]
    index = 0
    for i in range(len(s)):
        if small > s[i]:
            small = s[i]
            index = i

    return small, index


SEED, MIN, MAX, N = map(int, input().split(' '))

random.seed(SEED)

S = random.sample(range(MIN, MAX), N)
print(*find_min(S))
