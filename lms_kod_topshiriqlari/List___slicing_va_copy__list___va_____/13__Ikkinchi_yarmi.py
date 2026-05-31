n = int(input())
sonlar = list(map(int, input().split()))
ikkinchi_yarim = sonlar[(n + 1) // 2:]
print(ikkinchi_yarim)