import random

SEED, MIN, MAX, N = 2022, 10, 100, 8
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)

print(S)
print(sorted(S))
print(S)
S.sort()
print(S)

print('#' * 20)

S = random.sample(range(MIN, MAX), N)
print(S)
print(sorted(S, reverse=True))
S.sort(reverse=True)
print(S)
