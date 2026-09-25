# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - median toping:
#   * agar count toq bo‘lsa: o‘rtadagi element
#   * agar count juft bo‘lsa: o‘rtadagi 2 ta element o‘rtachasi
# OUTPUT: median ni 2 kasr bilan chiqaring
# Eslatma: sonlarni sorted qilib oling
sonlar = list(map(int , input().split()))
sonlar.sort()
n = len(sonlar)
if n % 2 != 0:
    mediana = sonlar[n // 2]
else:
    mediana = (sonlar[n // 2 - 1] + sonlar [ n // 2]) / 2
print(f"{mediana:.2f}")