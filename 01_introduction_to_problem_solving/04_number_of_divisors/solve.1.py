import time


def solve(N):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
    return count


N = int(input())

start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time: {end - start}')
