# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - list: tartib bo‘yicha hamma so‘zlar (aslida bu input)
# - set: unique so‘zlar (lower)
# - dict: chastota
# Hisoblang:
# 1) total_count = so‘zlar soni
# 2) unique_count = unikal so‘zlar soni
# 3) top_word = eng ko‘p uchragan so‘z (teng bo‘lsa alifbo kichigi)
# OUTPUT (3 qator):
# total: N
# unique: U
# top: WORD COUNT
text = input()
words = text.lower().split()
total_count = len(words)
unique_words = set(words)
unique_count = len(unique_words)
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
top_word = min(unique_words, key=lambda w: (-freq[w], w))
print(f"total: {total_count}")
print(f"unique: {unique_count}")
print(f"top: {top_word} {freq[top_word]}")