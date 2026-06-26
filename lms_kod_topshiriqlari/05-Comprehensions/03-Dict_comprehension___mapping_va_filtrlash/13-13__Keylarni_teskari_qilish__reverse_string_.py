n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key[::-1]] = int(value)
print(d)
# INPUT:
# n
# n qator: key value
# VAZIFA: yangi dict: key'lar teskari yozilsin (key[::-1])
# value o‘zgarmasin
# OUTPUT: dict
