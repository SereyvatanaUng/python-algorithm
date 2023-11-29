# anagram nagaram
s, t = input().split()
if sorted(s) == sorted(t):
    print('true')
else:
    print('false')
