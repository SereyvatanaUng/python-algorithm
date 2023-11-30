import time

A, B, M = map(int, input().split())

start = time.time()

print(pow(A, B, M))

end = time.time()
print(f'solve() elapsed time: {end - start}')
