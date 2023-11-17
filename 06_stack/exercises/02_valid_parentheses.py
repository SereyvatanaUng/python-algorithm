# Valid Parentheses

# Given a string ‘s’ containing just the characters '(', ')', '{', '}', '[', ']', '<', '>', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

# Constraints:
# 1 ≤ s.length ≤ 10⁴
# s consists of parentheses only '()[]{}<>'.

# Input
# The parentheses '(', '), '{', '}', '[', ']', '<', and '>' are randomly combined and given.

# Output
# Verify that the entered parentheses string is correct, output 'True' if correct, or 'False' if not.

# Sample Input 1
# (({})[()]{})

# Sample Output 1
# True


def solve(S):
    opening = "<[{("
    closing = ">]})"
    stack = []
    for s in S:
        if s in opening:
            stack.append(s)
        elif stack and opening.index(stack[-1]) == closing.index(s):
            stack.pop()
        else:
            return False
    return len(stack) == 0


S = input()
print(solve(S))
