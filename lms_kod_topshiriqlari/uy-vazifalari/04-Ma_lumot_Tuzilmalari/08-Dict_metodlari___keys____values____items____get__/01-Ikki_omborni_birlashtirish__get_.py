ombor = {}
for _ in range(int(input())):
    nomi, miqdori = input().split()
    ombor[nomi] = ombor.get(nomi, 0) + int(miqdori)
for _ in range(int(input())):
    nomi, miqdori = input().split()
    eski_miqdori = ombor.pop(nomi, 0)
    ombor[nomi] = eski_miqdori + int(miqdori)
for nomi, miqdori in ombor.items():
    print(nomi, miqdori)