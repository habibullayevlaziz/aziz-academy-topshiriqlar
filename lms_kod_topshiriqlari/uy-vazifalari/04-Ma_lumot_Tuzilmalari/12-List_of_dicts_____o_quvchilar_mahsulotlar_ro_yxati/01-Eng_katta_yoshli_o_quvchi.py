n = int(input())
students = []
for _ in range(n):
    name, age = input().split()
    students.append({"name": name, "age": int(age)})
oldest_student = max(students, key=lambda s: s["age"])
print(oldest_student["name"])