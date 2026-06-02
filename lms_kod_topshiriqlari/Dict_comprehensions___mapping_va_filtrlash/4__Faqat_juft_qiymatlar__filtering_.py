n = int(input())
data = {}
for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
result = {key: value for key, value in data. items() if value % 2 == 0}
print(result)
# INPUT:
# n
# n qator: key value
# VAZIFA: faqat juft value (value % 2 == 0) bo‘lganlarini qoldiring
# OUTPUT: dict
