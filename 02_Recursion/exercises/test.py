def count_triangles(n, sides=[]):
    if len(sides) == 3:
        # Check if these sides can form a triangle
        if sum(sides) == n:
            return 1
        return 0

    count = 0
    for side in range(1, n + 1):
        new_sides = sides + [side]

        # Check if the current combination is valid so far
        if len(new_sides) == 3 and sum(new_sides) != n:
            continue
        if len(new_sides) == 2 and 2 * max(new_sides) <= n:
            continue

        count += count_triangles(n, new_sides)

    return count


n = int(input("Enter the number n: "))
total_triangles = count_triangles(n)
print(
    f"Number of triangles that can be formed with the given sum: {total_triangles}")
