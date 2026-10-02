n = int(input())
d = {}
for _ in range(n):
    nomi, narxi = input().split()
    d[nomi] = int(narxi)
print(sum(d.values()))