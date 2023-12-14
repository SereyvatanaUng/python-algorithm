def solve(n, a):
    if n <= 0:
        return 0
    else:
        return a[n] + max(solve(n-1, a), solve(n-2, a))


N = int(input())
A = [0] + list(map(int, input().split()))
print(solve(N, A))
