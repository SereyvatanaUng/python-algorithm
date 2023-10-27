# Read the three integers from the input
a, b, c = map(int, input().split())

# Create a list of all integers from -100 to 100
all_integers = list(range(-100, 101))

# Remove the three integers from the list
all_integers.remove(a)
all_integers.remove(b)
all_integers.remove(c)

# Sort the remaining list
all_integers.sort()

# Initialize a variable to store the missing integer
missing_integer = None

# Iterate through the sorted list to find the missing integer
for i in range(1, len(all_integers)):
    if all_integers[i] - all_integers[i-1] != 1:
        missing_integer = all_integers[i-1] + 1

# If the missing integer is at the boundaries, update it accordingly
if missing_integer is None:
    if all_integers[0] > 1:
        missing_integer = all_integers[0] - 1
    elif all_integers[-1] < 100:
        missing_integer = all_integers[-1] + 1

# Print the missing integer
print(missing_integer)
