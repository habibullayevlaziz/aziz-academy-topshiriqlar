# INPUT:
# 1-qator: n
# keyingi n qator: name score
# VAZIFA:
# - har o‘quvchini dict ko‘rinishida saqlang: {'name':..., 'score':...}
# - eng katta score toping
# - agar teng bo‘lsa name kichigi yutsin
# OUTPUT: name score
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
eng = students[0]
for o in students:
    if o['score'] > eng['score'] or (o['score'] == eng['score'] and o['name'] < eng['name']):
        eng = o
print(eng['name'], eng['score'])