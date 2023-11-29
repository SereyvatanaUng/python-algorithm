# Kangaroo

# Description
# Three kangaroos are playing in the grassland. They lie on a straight line at different integer coordinates A(0<A<100) and B(0<B<100) and C(0<C<100). On the first line, print the maximum number of jumps the kangaroo can make.

# Only one kangaroo standing outside at a time can jump in between two kangaroos. Two kangaroos cannot be located at the same coordinates at the same time.


# Input
# The integer coordinates A, B, and C with three kangaroos in the first row are given.


# Output
# On the first line, print the maximum number of jumps the kangaroo can make.


# Sample Input 1
# 2 3 5

# Sample Output 1
# 1

N = list(map(int, input().split()))
cnt = 0

while True:
    if N[0] > N[1]:
        cnt += 1
        N[0], N[1] = N[1], N[0]
        continue
    elif N[2] > N[1]:
        cnt += 1
        N[1], N[2] = N[2], N[1]
        continue
    else:
        break

print(cnt)
