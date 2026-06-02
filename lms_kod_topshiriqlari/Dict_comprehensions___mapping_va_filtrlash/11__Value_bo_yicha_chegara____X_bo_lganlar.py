n = int(input())
d = {}
items = []
for _ in range(n):
    key, value = input().split()
    items.append((key, int(value)))
X = int(input())
for key, value in items:
    if value >= X:
        d[key] = value
print(d)
# INPUT:
# 1-qator: n
# n qator: key value
# oxirgi qator: X
# VAZIFA: faqat value >= X bo‘lgan juftliklardan dict tuzing
# OUTPUT: dict
