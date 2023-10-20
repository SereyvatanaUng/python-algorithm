# sample input 1
# 100
# sample output 1
# 5050

def sum_num(n):
    if n == 1:
        return 1
    return n + sum_num(n - 1)


N = int(input())
print(sum_num(N))
