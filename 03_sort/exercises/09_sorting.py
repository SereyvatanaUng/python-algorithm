N = int(input())
arr = list(map(int, input().split()))

for i in arr:
    print(i, end=" ")
print()
print(*sorted(arr))
