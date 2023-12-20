def solve(k, coins):
    change = []
    for i in range(len(coins)):
        change += [coins[i]] * (k//coins[i])
        k = k % coins[i]
        if k == 0:
            break
    return len(change), change


K = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
opt, change = solve(K, coins)
print(opt)
print(*sorted(change))
