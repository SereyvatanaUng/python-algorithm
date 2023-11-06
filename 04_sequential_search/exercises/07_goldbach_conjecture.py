# The Goldbach Conjecture
# Description

# Mathematician Goldbach made the following conjecture.

# Goldbach's Conjecture: Any even integer greater than 2 can be expressed as the sum of two prime numbers.


# Weak Goldbach's Conjecture: Any odd integer greater than 5 can be expressed as the sum of three prime numbers.

# According to Goldbach's weak conjecture, any odd number greater than 5 can be expressed as the sum of three prime numbers. At this time, if a triangle can be created with these three prime numbers, let's call this triangle a Goldbach triangle.

# For example, if N = 7, N = 2 + 2 + 3, then N can be expressed as the sum of three prime numbers (2, 2, 3). Therefore, we can create a Goldbach triangle with three sides of 2, 2, and 3, respectively.

# However, if N = 9, N = 2 + 2 + 5, it can be expressed as three prime numbers (2, 2, 5). However, since a triangle cannot be created with numbers whose three sides are 2, 2, and 5, respectively, a Goldbach triangle cannot be created. Instead, since N = 3 + 3 + 3, we can create a Goldbach triangle with sides of 3, 3, and 3, respectively.

# Given N random odd numbers greater than 5, print the number of different Goldbach triangles that can be created. In other words, when 7 = 2 + 2 + 3, (2, 2, 3) and (3, 2, 2) are the same combination, they are counted as one.


# Input
# In the first line, a positive integer N is given.
# In the second line, N odd numbers M greater than 5 and less than 10,000 are given.

# 5<M<10,000, M%2=1

# Output

# Prints the number of Goldbach triangles that can be created with the odd number given in the first line.


# Sample Input 1
# 5 7 9 11 13 15

# Sample Output 1
# 1 1 1 1 2
