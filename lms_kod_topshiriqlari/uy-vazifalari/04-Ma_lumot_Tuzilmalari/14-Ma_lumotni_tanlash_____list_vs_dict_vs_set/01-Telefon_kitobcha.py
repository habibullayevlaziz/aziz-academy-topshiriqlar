n = int(input())
daftar = dict(input().split() for _ in range(n))
m = int(input())
for _ in range(m):
    print(daftar.get(input(), "topilmadi"))