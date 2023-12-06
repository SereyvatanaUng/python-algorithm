N, M = 10 ** 6, 10 ** 6

A = " ".join(str(i) for i in range(1, N + 1))
B = " ".join(str(i) for i in range(N + 1, N + M + 1))

file_path = "4.in"

with open(file_path, "w") as f:
    f.write(f"{N} {M}\n")
    f.write(f"{A}\n")
    f.write(f"{B}\n")
