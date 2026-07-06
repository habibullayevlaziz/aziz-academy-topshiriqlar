import sys
x1, y1, x2, y2 = map(int,sys.stdin.read().split())
res = (x2 - x1) ** 2 + (y2 - y1)**2
print(res)