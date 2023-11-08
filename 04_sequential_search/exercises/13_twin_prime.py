def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def twin():
    arr = []
    for i in range(101):
        if is_prime(i):
            arr.append(i)

    for j in range(1, len(arr)):
        if arr[j] - arr[j - 1] == 2:
            print(arr[j], arr[j - 1])


twin()
