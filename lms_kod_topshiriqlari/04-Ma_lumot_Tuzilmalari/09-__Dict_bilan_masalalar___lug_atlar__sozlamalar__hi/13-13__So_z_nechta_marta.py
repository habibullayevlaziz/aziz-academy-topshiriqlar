# Kodingizni shu yerga yozing
n = int(input())
d = {}
for i in range(n):
    w = input()
    d[w] = d.get(w, 0) + 1
izlanadigan = input()
print(d.get(izlanadigan, 0))
