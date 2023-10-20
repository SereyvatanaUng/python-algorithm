def collatz_sequence_length(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def find_longest_collatz_sequence(N, M):
    max_length = -1
    result_number = -1
    for number in range(N, M + 1):
        length = collatz_sequence_length(number)
        if length > max_length:
            max_length = length
            result_number = number
        elif length == max_length:
            result_number = max(result_number, number)
    return result_number


N = int(input("Enter N: "))
M = int(input("Enter M: "))
result = find_longest_collatz_sequence(N, M)
print(
    f"The number with the longest Collatz sequence in the range [{N}, {M}] is: {result}")
