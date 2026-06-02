n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    value = int(value)
    if value % 2 == 0:
        d[key] = "even"
    else:
        d[key] = "odd"
print(d)
