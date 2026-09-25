import math
n = int(input())
t = int(input())
katakchalar_soni = 0
for i in range(1, n + 1):
    ekub = math.gcd(i, t)
    kerakli_pogona = t // ekub
    katakchalar_soni += n // kerakli_pogona
print(katakchalar_soni)