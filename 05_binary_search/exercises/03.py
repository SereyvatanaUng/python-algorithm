import random
SEED, N = 12345, 5001
random.seed(SEED)
S = sorted(random.sample(range(-N, 2*N, 2), N))
for i in range(len(S)):
    if i == S[i]:
        print(S[i])
