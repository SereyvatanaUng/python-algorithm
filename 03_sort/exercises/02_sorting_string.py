import random
from string import ascii_lowercase


def generate(SEED, N, index):
    random.seed(SEED)
    S = []
    for _ in range(N):
        length = random.randint(1, N-1)
        s = random.sample(ascii_lowercase, length)
        S.append("".join(s))
    return S[index - 1]


a, b, c = map(int, input().split(' '))
# S = generate(2022, 10, 5)
S = generate(a, b, c)
print(S)
