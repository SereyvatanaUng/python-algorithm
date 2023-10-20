def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def lcm(x, y):
    return x * y // gcd(x, y)


def lcm_of_set_recursive(numbers, current_index=0):
    if current_index == len(numbers) - 1:
        return numbers[current_index]

    current_lcm = lcm(numbers[current_index], numbers[current_index + 1])
    remaining_numbers = [current_lcm] + numbers[current_index + 2:]

    return lcm_of_set_recursive(remaining_numbers, current_index)


# Input the set of positive integers
k = int(input("Enter the number of positive integers: "))
x = list(map(int, input("Enter the positive integers separated by spaces: ").split()))

# Calculate and print the LCM of the set
result_lcm = lcm_of_set_recursive(x)
print(f"The LCM of the set is: {result_lcm}")
