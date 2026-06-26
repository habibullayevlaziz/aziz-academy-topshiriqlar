n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[len(key)] = int(value)
print(d)
# INPUT:
# n
# n qator: key value
# VAZIFA: yangi dict: key o‘rniga key uzunligi (len(key)) bo‘lsin, value o‘zgarmasin
# DIQQAT: agar ikki key uzunligi bir xil bo‘lsa, oxirgisi qoladi (python dict xulqi)
# OUTPUT: dict
