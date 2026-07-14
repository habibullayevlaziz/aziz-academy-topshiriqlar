n = int(input())
lugat = {}
for _ in range(n):
    kalit, qiymat = input().split()
    lugat[kalit] = qiymat
qidirilayotgan = input()
if qidirilayotgan in lugat:
    print(lugat[qidirilayotgan])
else:
    print("Yo'q")