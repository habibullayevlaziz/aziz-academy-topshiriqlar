# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - musbatlar soni (x>0)
# - manfiylar soni (x<0)
# - nollar soni (x==0)
# OUTPUT:
# 1-qator: positives_count
# 2-qator: negatives_count
# 3-qator: zeros_count
sonlar = list(map(int, input().split()))
positives = sum(1 for x in sonlar if x > 0)
negatives = sum(1 for x in sonlar if x < 0)
zeros = sum(1 for x in sonlar if x == 0)
print(positives)
print(negatives)
print(zeros)