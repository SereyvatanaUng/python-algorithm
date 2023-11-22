# A Magic Wand

# Description

# Harry Potter's wand was damaged while fighting Lord Voldemort. So Harry Potter decided to purchase a new wand at Ollivander's Wand Shop with Euler. Ollivander's Wand Shop has N magic wands and N wand boxes. The lengths of the wands are, respectively, X1, X2, … , Xn, and the box sizes are Y1, Y2, … , Yn. A wand of length X can be placed in a box of size Y if X ≤ Y. Since a box can only hold one wand, Harry wants to know whether each box can hold all of the wands. Help Harry solve this difficult problem.

# Input
# In the first line, a single positive integer N (1≤N≤100) is given, representing the number of wands and boxes. In the second line, N positive integers Xi(1≤Xi≤10^9) is given, representing the length of the wands.In the third line, N positive integers Yi(1≤Yi≤10^9) is given, representing the size of the box.

# Output
# If Harry can put all of his wands in the box, print "YES" on the first line, and if Harry cannot, print "NO" on the first line.

# Sample Input 1
# 4
# 5 3 3 5
# 10 2 10 10

# Sample Output 1
# NO

N = int(input())
X = map(int, input().split())
Y = map(int, input().split())

if min(X) < min(Y):
    print("YES")
else:
    print("NO")
