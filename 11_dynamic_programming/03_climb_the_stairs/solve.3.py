dp = {0: 0}


def solve(n, a):
    if n == 1:
        dp[n] = a[n]
    elif n not in dp:
        dp[n] = a[n] + max(solve(n-1, a), solve(n-2, a))
    return dp[n]


N = int(input())
A = [0] + list(map(int, input().split()))
print(solve(N, A))
