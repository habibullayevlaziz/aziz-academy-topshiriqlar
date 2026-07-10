sonlar = sorted(map(int, input().split()))
n = len(sonlar)
if n % 2 != 0:
    print(sonlar[n // 2])
else:
    print((sonlar[n // 2 - 1] + sonlar[n // 2]) // 2)