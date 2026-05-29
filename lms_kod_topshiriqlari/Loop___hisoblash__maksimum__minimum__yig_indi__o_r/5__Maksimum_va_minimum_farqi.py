n = int(input())
sonlar = list(map(int, input().split()))
mx = sonlar[0]
mn = sonlar[0]
for i in range(1, n):
    if sonlar[i] > mx:
        mx = sonlar[i]
    if sonlar[i] < mn:
        mn = sonlar[i]
print(mx - mn)

