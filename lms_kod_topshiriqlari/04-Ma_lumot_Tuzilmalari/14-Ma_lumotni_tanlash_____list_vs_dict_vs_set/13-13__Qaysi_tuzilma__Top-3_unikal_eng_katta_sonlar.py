# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - unikal qiling (set)
# - kamayish bo‘yicha sort qiling
# - top-3 ni oling (agar kam bo‘lsa borini)
# OUTPUT: sonlarni space bilan chiqarish (desc)
sonlar = list(map(int, input().split()))
unikal = sorted(set(sonlar), reverse=True)
print(" ".join(str(x) for x in unikal[:3]))