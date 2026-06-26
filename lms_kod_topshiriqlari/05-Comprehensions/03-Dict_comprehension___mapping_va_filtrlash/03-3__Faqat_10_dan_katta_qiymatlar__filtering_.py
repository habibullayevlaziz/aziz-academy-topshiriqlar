n = int(input())
data = {}
for _ in range(n):
    key, value = input().split()
    data[key] = int(value)
result = {key: value for key, value in data.items() if value > 10}
print(result)
# INPUT:
# n
# n qator: key value
# VAZIFA: faqat value > 10 bo‘lgan juftliklarni qoldiring
# OUTPUT: yangi dict
