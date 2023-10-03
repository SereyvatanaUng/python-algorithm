import time


def solve(n):
    count = 0
    sqrtn = int(n ** 0.5)

    for i in range(1, sqrtn + 1):
        if n % i == 0:
            count += 2

    if sqrtn * sqrtn == n:
        count -= 1

    return count


N = int(input())

start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time: {end - start}')
