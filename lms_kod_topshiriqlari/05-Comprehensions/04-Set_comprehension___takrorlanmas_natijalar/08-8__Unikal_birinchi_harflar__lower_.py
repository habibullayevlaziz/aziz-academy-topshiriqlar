words = input().split()
letters = sorted({word[0].lower() for word in words})
print(*letters)
# INPUT: 1 qatorda so‘zlar
# VAZIFA: har bir so‘zning 1-harfini (lower) setga oling
# OUTPUT: harflarni alifbo bo‘yicha sorted qilib space bilan chiqaring
# Masalan: Ali Vali hasan -> a h v
