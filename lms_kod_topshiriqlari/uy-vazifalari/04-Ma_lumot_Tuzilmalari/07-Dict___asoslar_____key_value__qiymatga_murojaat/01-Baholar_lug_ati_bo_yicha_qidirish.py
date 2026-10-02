n = int(input())
students = {}
for _ in range(n):
    name, score = input().split()
    students[name] = int(score)
name = input()
print(students[name])