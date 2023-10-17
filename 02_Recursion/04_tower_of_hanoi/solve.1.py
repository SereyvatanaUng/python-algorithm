######################
# Debug
# def hanoi(n, src, via, dst, x):

#     if n == 1:
#         print(n, src, via, dst, x)
#         print(f"{src} -> {dst}\n")

#     else:
#         hanoi(n - 1, src, dst, via, '	else 1')
#         hanoi(1, src, via, dst, '	else 2')
#         hanoi(n - 1, via, src, dst, '	else 3')


# N = int(input())
# hanoi(N, 'A', 'B', 'C', '	initial')


def hanoi(n, src, via, dst):
    print(n, src, via, dst)

    if n == 1:
        print(f"{src} -> {dst}\n")

    else:
        hanoi(n - 1, src, dst, via)
        hanoi(1, src, via, dst)
        hanoi(n - 1, via, src, dst)


N = int(input())
hanoi(N, 'A', 'B', 'C')
