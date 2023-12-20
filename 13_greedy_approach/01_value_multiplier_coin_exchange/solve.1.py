def solve(k, i, coins):
    if k == 0:
        return 0, []
    else:
        if k >= coins[i]:
            opt, change = solve(k - coins[i], i, coins)
            return opt + 1, change + [coins[i]]
        else:
            opt, change = solve(k, i+1, coins)
            return opt, change


K = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
opt, change = solve(K, 0, coins)
print(opt)
print(*sorted(change))
