# INPUT:
# 1-qator: n
# keyingi n qator: name score
# keyingi qator: q
# keyingi q qator: name
# VAZIFA:
# - name->score dict tuzing
# - so‘rovdagi name bo‘lsa score chiqarilsin, bo‘lmasa: NOT_FOUND
# OUTPUT: har query uchun javob alohida qatorda
n = int(input())
baholar = {}
for _ in range(n):
    name, score = input().split()
    baholar[name] = int(score)
q = int(input())
for _ in range(q):
    name = input().strip()
    if name in baholar:
        print(baholar[name])
    else:
        print("NOT_FOUND")