n = int(input())
max_k = -1
best_course = ""
for _ in range(n):
    data = input().split()
    course_name = data[0]
    k = int(data[1])
    if k > max_k:
        max_k = k
        best_course = course_name
print(best_course)