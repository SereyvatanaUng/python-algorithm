# Selection Sort Order

# Description
# When sorting N different positive integers using selection sort, Print the two numbers that are swapped for the Kth time.
# However, the selection sort algorithm uses the selectionsort() function implemented in Example 3.6.


# Input
# The first line is given positive integers N and K.
# The second line is given N different integers.


# Output
# The first line outputs the two numbers swapped in the Kth order in ascending order.

# Sample Input 1
# 7 10
# 50 40 70 10 30 20 60

# Sample Output 1
# 50 70


def selectionsort(s, a, b):
    cnt = 0
    n = 7
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]  # swap
                cnt += 1
            if cnt == a:
                print(s[j+1], end=" ")
            if cnt == b:
                print(s[j+5])


A, B = map(int, input().split())
S = list(map(int, input().split()))
selectionsort(S, A, B)
