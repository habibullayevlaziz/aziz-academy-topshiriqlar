n = int(input())
sonlar = [input().strip() for _ in range(n)]
for son in sonlar:
    print(son.rjust(6))