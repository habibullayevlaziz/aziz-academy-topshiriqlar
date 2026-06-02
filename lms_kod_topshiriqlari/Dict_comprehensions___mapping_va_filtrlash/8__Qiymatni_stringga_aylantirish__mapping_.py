n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = str(int(value))
print(d)
# INPUT:
# n
# n qator: key value
# VAZIFA: value ni str(value) qilib yangi dict yarating
# OUTPUT: dict
