# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - juft sonlar soni (evens_count)
# - toq sonlar soni (odds_count)
# OUTPUT:
# 1-qator: evens_count
# 2-qator: odds_count
sonlar = list(map(int, input().split()))
evens = sum(1 for x in sonlar if x % 2 == 0)
odds = sum(1 for x in sonlar if x % 2 != 0)
print(evens)
print(odds)