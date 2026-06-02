n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    value = abs(int(value))
    if value >= 5:
        d[key] = value
print(d)