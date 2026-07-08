n = int(input())
ombor = {}
for _ in range(n):
    nomi, miqdori = input().split()
    ombor[nomi] = ombor.get(nomi, 0) + int(miqdori)
for nomi, miqdori in ombor.items():
    print(nomi, miqdori)