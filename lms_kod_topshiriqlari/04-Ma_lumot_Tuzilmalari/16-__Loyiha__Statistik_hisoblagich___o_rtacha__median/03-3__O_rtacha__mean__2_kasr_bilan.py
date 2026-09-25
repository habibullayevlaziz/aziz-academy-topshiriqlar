# INPUT: 1 qatorda butun sonlar
# VAZIFA: o‘rtacha qiymatni (mean) hisoblang: sum/count
# OUTPUT: mean ni 2 kasr bilan chiqaring
# Masalan: 1 2 3 -> 2.00
sonlar = list(map(int, input().split()))
mean_val = sum(sonlar) / len(sonlar)
print(f"{mean_val:.2f}")