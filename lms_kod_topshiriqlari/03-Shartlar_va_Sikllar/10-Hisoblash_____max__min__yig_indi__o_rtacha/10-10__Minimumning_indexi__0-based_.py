n = int(input())
sonlar = list(map(int, input().split()))
son = 0
for i in sonlar:
    son += 1
if son > 2:
    print(sonlar[0])
else:
    print(0)
