n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = f"{key}:{value}"
print(d)
# INPUT:
# n
# n qator: key value
# VAZIFA: yangi dict: value o‘rniga "key:value" ko‘rinishidagi string bo‘lsin
# Masalan: a 2 -> {'a': 'a:2'}
# OUTPUT: dict
