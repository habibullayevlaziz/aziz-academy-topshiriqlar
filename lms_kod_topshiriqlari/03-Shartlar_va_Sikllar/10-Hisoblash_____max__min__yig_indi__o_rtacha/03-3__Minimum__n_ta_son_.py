n = int(input())
sonlar = list(map(int, input().split()))
min = sonlar[0]
for i in range(1, n):
    if sonlar[i] < min:
        min = sonlar[i]
print(min)
