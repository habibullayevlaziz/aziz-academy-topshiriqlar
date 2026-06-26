n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    if key.startswith('a'):
        d[key] = int(value)
print(d)
# INPUT:
# n
# n qator: key value
# VAZIFA: faqat key 'a' harfi bilan boshlansa qoldiring (key.startswith('a'))
# OUTPUT: dict
