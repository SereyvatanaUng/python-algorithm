N = int(input())
grade = {}
for _ in range(N):
    key, value = input().split()
    grade[key] = int(value)

sorted_grade = {k: v for k, v in sorted(
    grade.items(), key=lambda item: item[1], reverse=True)}

print(*sorted_grade.keys())
