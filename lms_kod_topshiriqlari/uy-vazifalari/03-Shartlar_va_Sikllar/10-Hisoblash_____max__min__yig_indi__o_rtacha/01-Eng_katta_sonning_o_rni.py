n = int(input())
sonlar = [int(input()) for _ in range(n)]
print(sonlar.index(max(sonlar)) + 1)