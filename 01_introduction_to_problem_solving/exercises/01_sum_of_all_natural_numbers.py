# sample input 1
# 1 100
# sample output 1
# 5050

def sum_num(n, m):
    return (m * (m + 1) // 2) - (n * (n - 1) // 2)


N, M = map(int, input().split(' '))
print(sum_num(N, M))
