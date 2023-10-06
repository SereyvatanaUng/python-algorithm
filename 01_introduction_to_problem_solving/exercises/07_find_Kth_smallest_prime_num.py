# sample input 1
# 1 10 3
# sample output 1
# 17
# 5


def find_k(a, b, k):
    s = 0
    cnt = 0
    for i in range(a, b + 1):
        is_prime = True
        if i <= 1:
            continue

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            s += i
            cnt += 1
            if cnt == k:
                index = i

    return s, index


A, B, K = map(int, input().split(' '))
sum_prime, k_index = find_k(A, B, K)
print(sum_prime)
print(k_index)
