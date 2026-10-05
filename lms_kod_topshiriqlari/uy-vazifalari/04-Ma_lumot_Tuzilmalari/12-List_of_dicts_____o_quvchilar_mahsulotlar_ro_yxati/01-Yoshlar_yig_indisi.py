n = int(input())
students = []
for _ in range(n):
    name, age = input().split()
    students.append({"name": name, "age": int(age)})
total_age = sum(student["age"] for student in students)
print(total_age)