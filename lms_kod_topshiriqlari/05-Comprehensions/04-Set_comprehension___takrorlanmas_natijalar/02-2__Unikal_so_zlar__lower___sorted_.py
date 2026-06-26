words = input().split()
unique_words = {word.lower() for word in words}
sorted_words = sorted(unique_words)
print(*sorted_words)
# INPUT: 1 qatorda so‘zlar
# VAZIFA: hamma so‘zlarni lower() qilib unikal set qiling
# OUTPUT: unikal so‘zlarni alifbo bo‘yicha sorted qilib space bilan chiqaring
# Masalan: Ali ali VALI -> ali vali
