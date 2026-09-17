# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - dict bilan chastota sanang
# - faqat 1 marta uchragan sonlarni set/list qilib oling
# OUTPUT:
# - agar bo‘sh bo‘lsa: EMPTY
# - aks holda: sorted qilib space bilan chiqaring
sonlar = list(map(int, input().split()))
hisob = {}
for x in sonlar:
    hisob[x] = hisob.get(x, 0) + 1
yagona = []
for x in sorted(hisob):
    if hisob[x] == 1:
        yagona.append(x)
if yagona:
    print(" ".join(str(x) for x in yagona))
else:
    print("EMPTY")