n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value) ** 2
print(d)