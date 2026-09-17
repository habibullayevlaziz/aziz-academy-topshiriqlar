# INPUT:
# 1-qator: k (config soni)
# keyingi k qator: key value (value int)
# keyingi qator: q
# keyingi q qator: key
# VAZIFA:
# - config dict tuzing
# - so‘rovda key bo‘lsa qiymatini chiqarish
# - bo‘lmasa default 0 chiqarish
# OUTPUT: har query uchun int
k = int(input())
config = {}
for _ in range(k):
    kalit, qiymat = input().split()
    config[kalit] = int(qiymat)
q = int(input())
for _ in range(q):
    kalit = input().strip()
    print(config.get(kalit, 0))