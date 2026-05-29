n = int(input())
sonlar = list(map(int, input().split()))
x = int(input())
topildi = -1
for i in range(len(sonlar)):
    if sonlar[i] == x:
        topildi = i
        break
print(topildi)
