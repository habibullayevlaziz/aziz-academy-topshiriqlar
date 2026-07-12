sonlar = list(map(int, input().split()))
sonlar.sort()
n = len(sonlar)
print(sonlar[n // 2])