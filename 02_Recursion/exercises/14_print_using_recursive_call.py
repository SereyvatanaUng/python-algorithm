# sample input 1
# 20
# sample output
# 0
# 1
# ...
# 20

def recur_call(n):
    if n == 0:
        print(n)
        return
    recur_call(n - 1)
    print(n)


N = int(input())
recur_call(N)
