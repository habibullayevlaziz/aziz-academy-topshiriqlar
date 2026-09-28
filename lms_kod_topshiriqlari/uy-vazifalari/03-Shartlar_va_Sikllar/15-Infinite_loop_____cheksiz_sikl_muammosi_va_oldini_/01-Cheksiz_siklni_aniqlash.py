import math
start = int(input())
step = int(input())
if start >= 100:
    print(0)
elif step <= 0:
    print("CHEKSIZ")
else:
    qadamlar = math.ceil((100 - start) / step)
    print(qadamlar)