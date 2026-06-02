n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key.upper()] = int(value)
print(d)
