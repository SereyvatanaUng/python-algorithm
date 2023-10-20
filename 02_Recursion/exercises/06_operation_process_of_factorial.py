# sample input 4
# sample output 1*2*3*4

def fact(n):
    if n == 1:
        return 1
    else:
        return str(fact(n-1)) + '*' + str(n)


N = int(input())
print(fact(N))
