# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - dict bilan chastota sanang (lower)
# - eng ko‘p uchragan so‘zni toping
# - agar teng bo‘lsa: alifbo bo‘yicha kichigi yutsin
# OUTPUT: word count
sozlar = input().lower().split()
hisob = {}
for s in sozlar:
    hisob[s] = hisob.get(s, 0) + 1
eng = None
for s in sorted(hisob):
    if eng is None or hisob[s] > hisob[eng]:
        eng = s
print(eng, hisob[eng])