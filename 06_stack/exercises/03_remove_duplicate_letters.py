# Remove Duplicate Letters

# Description
# Given a stringsas input, remove the duplicate and print out all the types of characters in the string, separated by commas (','). You must make sure your result is the smallest in lexicographical order among all possible results.

# Constraints:
# 1 ≤ s.length ≤ 10⁴
# sconsists of lowercase English letters.


# Input
# Given a stringsas input.


# Output
# Characters included in the string are outputted separated by commas for each type.


# Sample Input 1
# aoidbibi

# Sample Output 1
# a,o,d,b,i


def solve(S):
    stack = []
    temp = []

    for s in S:
        if s not in stack:
            stack.append(s)
        else:
            while s != stack[-1]:
                temp.append(stack.pop())
            stack.pop()
            temp.reverse()
            stack += temp
            stack += [s]
            temp = []

    result = ",".join(stack)
    return result


S = input()
print(solve(S))
