# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - so‘zlarni lower qilib setga o‘tkazing (unikal)
# - sorted qilib chiqarish
# OUTPUT: unikal so‘zlar alifbo bo‘yicha
text = input()
unique_words = set(text.lower().split())
sorted_words = sorted(unique_words)
print(*sorted_words)