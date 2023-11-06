# The number of Palindromes
# Description

# Given positive integers N and M, among numbers greater than or equal to N and less than or equal to M, print the number of palindromes in which the sum of each digit is a prime number.


# Input

# The first line is given positive integers N and M.


# Output

# Outputs the number of palindromes of which the sum of each digit is prime among the numbers greater than or equal to N and less than or equal to M.


# Sample Input 1
# 1 100

# Sample Output 1
# 5

def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)


def prime_digit(m):
    m = [int(digit) for digit in str(m)]
    n = sum(m)
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(N, M):
    cnt = 0
    for i in range(N, M + 1):
        if is_palindrome(i) and prime_digit(i):
            cnt += 1
    return cnt


N, M = map(int, input().split())
print(solve(N, M))
