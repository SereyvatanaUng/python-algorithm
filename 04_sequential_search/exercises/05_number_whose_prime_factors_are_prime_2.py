# A Number whose Prime Factors are Prime(2)
# Description

# Given a list S of integers composed of N integers, print the number of elements in S whose prime factors are prime. In this problem, N can be given a very large value, and the element value of S can also be given a very large value. Therefore, since the general prime factorization method takes too long, prime factorization using the Sieve of Eratosthenes method must be used.

# A list of random integers S can be generated using the following code. Using the seed() and sample() functions of Python's random module, you can generate random integers with certain rules.


# import random

# def generate(SEED, MIN, MAX, N):
#   random.seed(SEED)
#   return random.sample(range(MIN, MAX), N)
# SEED, MIN, MAX, N=2022,10,100,15
# S=generate(SEED, MIN, MAX, N)
# print(S)

# [78, 46, 66, 79, 49, 84, 17, 76, 98, 62, 97, 91, 50, 11, 65]


# Input

# In the first line, SEED, MIN, MAX, and N, which will generate the integer list S, are given in order.


# Output

# The first line prints the number of numbers whose prime factors are prime in the integer list S.


# Sample Input 1
# 2022 10 100 15

# Sample Output 1
# 10

import random


def factorize(n, m):
    if n < 2:
        return []
    elif m > int(n ** 0.5):
        return [n]
    elif n % m == 0:
        return [m] + factorize(n // m, m)
    else:
        return factorize(n, m + 1)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(S):
    cnt = 0
    for i in S:
        factors = factorize(i, 2)
        print(i, factors)
        if len(factors) > 1:
            cnt += 1
    return cnt


def generate(SEED, MIN, MAX, N):
    random.seed(SEED)
    return random.sample(range(MIN, MAX), N)


SEED, MIN, MAX, N = 2022, 10, 100, 15

S = generate(SEED, MIN, MAX, N)
print(solve(S))
