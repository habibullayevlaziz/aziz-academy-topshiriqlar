n = int(input())
d = {}
for i in range(n):
    kalit, qiymat = input().split()
    d[kalit] = qiymat
qidirilayotgan = input()
print(d.get(qidirilayotgan, "Topilmadi"))