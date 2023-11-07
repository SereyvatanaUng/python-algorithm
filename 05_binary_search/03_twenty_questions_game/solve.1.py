import random


def solve(x, s, t):
    low = s
    high = t
    while low < high:
        print(low, high, end=" ")
        mid = (low + high) // 2
        print(f"Bigger than {mid}?", end=" ")
        if x > mid:
            print("Yes.")
            low = mid + 1
        else:  # x < mid
            print("No.")
            high = mid
    print(f"Your X is {low}.")
    return low


S, T = map(int, input().split())
SEED = int(input())
random.seed(SEED)
X = random.randint(S, T)
solve(X, S, T)
