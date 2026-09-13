# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - list sifatida qabul qiling (tartib muhim)
# - birinchi 3 ta so‘zni (agar kam bo‘lsa borini) chiqaring
# OUTPUT: shu so‘zlarni space bilan chiqarish
sozlar = input().split()
print(" ".join(sozlar[:3]))