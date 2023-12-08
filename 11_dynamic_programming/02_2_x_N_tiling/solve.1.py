def solve(n):
    if n <= 2:
        return n
    else:
        return (solve(n-1) + solve(n-2)) % 10007
    
    
N = int(input())
print(solve(N))