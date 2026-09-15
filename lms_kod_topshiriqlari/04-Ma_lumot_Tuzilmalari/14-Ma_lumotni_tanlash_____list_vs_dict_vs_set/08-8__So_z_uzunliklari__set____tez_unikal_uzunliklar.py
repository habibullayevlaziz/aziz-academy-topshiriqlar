# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - har bir so‘z uzunligini setga o‘tkazing
sozlar = input().split()
uzunliklar = set()
for s in sozlar:
    uzunliklar.add(len(s))
print(" ".join(str(x) for x in sorted(uzunliklar)))
