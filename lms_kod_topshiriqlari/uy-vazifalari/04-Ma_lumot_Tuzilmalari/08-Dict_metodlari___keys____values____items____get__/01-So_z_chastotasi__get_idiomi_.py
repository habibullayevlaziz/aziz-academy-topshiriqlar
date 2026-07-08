mahsulotlar = input().split()
ombor = {}
for nomi in mahsulotlar:
    ombor[nomi] = ombor.get(nomi, 0) + 1
for nomi in sorted(ombor.keys()):
    print(nomi, ombor[nomi])