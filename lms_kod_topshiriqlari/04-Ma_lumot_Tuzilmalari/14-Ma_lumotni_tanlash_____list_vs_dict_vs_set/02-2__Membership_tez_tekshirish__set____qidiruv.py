# INPUT:
# 1-qator: n (sonlar soni)
# 2-qator: n ta butun son
# 3-qator: q (so‘rovlar soni)
# Keyingi q qator: bitta son (query)
# VAZIFA:
# - sonlarni setga o‘tkazing
# - har query uchun: agar set ichida bo‘lsa YES, bo‘lmasa NO
# OUTPUT: har query uchun alohida qatorda YES/NO
n = int(input())
sonlar = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    x = int(input())
    if x in sonlar:
        print("YES")
    else:
        print("NO")