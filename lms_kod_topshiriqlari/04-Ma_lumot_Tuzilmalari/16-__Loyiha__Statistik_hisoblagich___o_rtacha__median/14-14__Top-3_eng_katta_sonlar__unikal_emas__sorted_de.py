# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - sonlarni kamayish tartibida saralang
# - birinchi 3 tasini oling (agar 3 tadan kam bo‘lsa, borini oling)
# OUTPUT: top sonlarni space bilan chiqaring
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
top_3 = numbers[:3]
print(" ".join(map(str, top_3)))