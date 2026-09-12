# INPUT: 1 qatorda so‘zlar (space bilan)
# VAZIFA:
# - har bir so‘z (lower qilib) necha marta uchrashini dict orqali sanang
# OUTPUT:
# - har bir unikal so‘zni alifbo bo‘yicha sorted qilib chiqaring
# - format: word count
# Har biri yangi qato
sozlar = input().split()
hisob = {}
for s in sozlar:
    s = s.lower()
    hisob[s] = hisob.get(s, 0) + 1
for s in sorted(hisob.keys()):
    print(f"{s} { hisob[s]}")