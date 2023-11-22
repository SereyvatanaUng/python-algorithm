# Four Integers

# Description
# While carrying out academic research for the future of the kingdom, Euler discovered four important integers. What is even more surprising is that when four integers are sorted in such a way, the differences between neighboring integers are equal. One day, Euler lost one of the four integers, and the remaining three integers were not sorted.

# Given three integers in the range between -100 and 100 separated by a space, find the one integer that Euler missed in his four-square identity. If there are multiple possible correct answers, select the highest value and print it.

# Input
# Given three integers in the range between -100 and 100 separated by a space.

# Output
# Find and print the one integer that Euler missed.


# Sample Input 1
# 10 1 4

# Sample Output 1
# 7

s = list(map(int, input().split()))
s.sort()
n = 0
while True:
    if s[0] - s[1] == n - s[2] or s[0] - n == s[1] - s[2]:
        s.append(n)
        s.sort()
        print(n)
        break
    n += 1
