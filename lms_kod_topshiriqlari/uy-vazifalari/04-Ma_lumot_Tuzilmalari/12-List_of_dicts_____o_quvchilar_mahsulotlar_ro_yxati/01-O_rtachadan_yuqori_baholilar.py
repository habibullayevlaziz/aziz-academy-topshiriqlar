n = int(input())
students = []
total_score = 0
for _ in range(n):
    line = input().split()
    name = line[0]
    score = float(line[1])
    students.append((name, score))
    total_score += score
avg = total_score / n
for name, score in students:
    if score > avg:
        print(name)