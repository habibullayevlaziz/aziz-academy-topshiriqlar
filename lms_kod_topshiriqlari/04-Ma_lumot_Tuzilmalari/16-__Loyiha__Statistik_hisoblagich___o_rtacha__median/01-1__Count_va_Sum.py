# INPUT: 1 qatorda butun sonlar (space bilan)
# VAZIFA:
# - sonlar sonini (count)
# - yig‘indini (sum)
# hisoblab chiqaring
# OUTPUT:
# 1-qator: count
# 2-qator: sum
sonlar = list(map(int, input().split()))
print(len(sonlar))
print(sum(sonlar))