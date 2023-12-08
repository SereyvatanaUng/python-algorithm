def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return s == r


N = input()
print(is_palindrome(N))
