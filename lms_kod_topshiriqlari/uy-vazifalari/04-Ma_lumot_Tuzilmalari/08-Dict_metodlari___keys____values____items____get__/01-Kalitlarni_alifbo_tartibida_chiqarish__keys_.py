n = int(input())
d = {}
for _ in range(n):
    data = input().split()
    if data:
        ism = data[0]
        baho = data[1]
        d[ism] = baho
print(" ".join(sorted(d.keys())))