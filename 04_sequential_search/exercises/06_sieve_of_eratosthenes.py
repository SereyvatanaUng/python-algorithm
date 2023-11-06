# Description

# def find_primes(n):
# 	sieve=[0,0]+[1]*(n-1)
# 	for i in range(2, int(n**0.5)+1):
# 		if sieve[i]==1:
# 			for j in range(i*i, n+1, i):
# 				sieve[j]=0
# 	return sieve

# Given positive integers N and K, print the Kth number to be erased from the Sieve of Eratosthenes. If K is greater than the number to be erased, output 0.

# However, a number that has already been erased by another number is not counted as a number being erased.

# For example, in the case of N=15, K=8, the erasing order is as follows.

# 4 6 8 10 12 14 9 15

# Following the example given above, 12 has already been erased by 2, so it is not counted as a number erased by 3. Therefore, the 8th number to be erased is 15.


# Input

# In the first line, a positive integer N, K, is given.1≤K<N≤10000


# Output

# Prints the K-th erased number on the first line.
# If K is greater than the number to be erased, 0 is output.


# Sample Input 1
# 10 7

# Sample Output 1
# 0


def find_primes(n):
    sieve = [0, 0]+[1]*(n-1)
    real_num = [int(i) for i in range(n + 1)]
    pop_num = []
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == 1:
            for j in range(i*i, n+1, i):
                sieve[j] = 0
                pop_num.append(real_num[j])
                real_num[j] = 0

    return pop_num


def solve(n, m):
    sieve = find_primes(n)
    if m > len(sieve):
        return 0
    return sieve[m]


N, M = map(int, input().split())
print(solve(N, M))
