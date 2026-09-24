n = int(input())
sonlar = [int(input()) for _ in range(n)]
musbat = sum(1 for x in sonlar if x > 0)
manfiy = sum(1 for x in sonlar if x < 0)
print(musbat, manfiy)