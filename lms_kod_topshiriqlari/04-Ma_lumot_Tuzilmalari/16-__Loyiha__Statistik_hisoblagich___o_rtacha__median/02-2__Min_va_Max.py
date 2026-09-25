# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - min (eng kichik)
# - max (eng katta)
# ni toping
# OUTPUT:
# 1-qator: min
# 2-qator: max
sonlar = list(map(int, input().split()))
print(min(sonlar))
print(max(sonlar))