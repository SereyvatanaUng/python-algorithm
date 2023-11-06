# Hexadecimal Palindrome
# Description

# Hexadecimal palindrome refers to a number that becomes a palindrome when a positive integer is expressed in hexadecimal.

# For example, the hexadecimal representation of 289 and 43962 is 121 and ABBA, so it is a hexadecimal palindrome. On the other hand, the hexadecimal representation of 291 and 43981 is 123 and ABCD, so it is not a hexadecimal palindrome.

# Given N positive integers, print the number of hexadecimal palindromes.


# Input

# In the first line, a positive integer N is given.
# The second line gives N positive integers.


# Output

# The first line prints the number of hexadecimal palindromes among N positive integers.


# Sample Input 1
# 7
# 3903 4090 1991 801 1365 899 55709

# Sample Output 1
# 5

def is_hex_palindrome(n):
    hex_string = hex(n)[2:]
    return hex_string == hex_string[::-1]


def count_hex_palindromes(numbers):
    count = 0
    for n in numbers:
        if is_hex_palindrome(n):
            count += 1
    return count


N = int(input())
arr = list(map(int, input().split()))
result = count_hex_palindromes(arr)
print(result)
