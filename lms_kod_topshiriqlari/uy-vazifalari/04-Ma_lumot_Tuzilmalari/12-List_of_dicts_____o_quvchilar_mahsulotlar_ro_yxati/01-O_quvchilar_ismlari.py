n = int(input())
students = []
for _ in range(n):
    name, age = input().split()
    students.append({"name": name, "age": int(age)})
for student in students:
    print(student["name"])