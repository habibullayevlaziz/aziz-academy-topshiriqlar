n = int(input())
d = {}
seen = set()
for _ in range(n):
    key, value = input().split()
    value = int(value)
    if value not in seen:
        d[key] = value
        seen.add(value)
print(d)