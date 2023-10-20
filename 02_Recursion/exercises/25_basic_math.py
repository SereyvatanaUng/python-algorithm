# Ax + By = C

def equa(a, b, c):
    x = 0
    y = 0
    while True:
        for y in range(x):
            if a * x + b * y == c:
                return x, y
        x += 1


A, B, C = map(int, input().split(' '))
x, y = equa(A, B, C)
print(x, y)
