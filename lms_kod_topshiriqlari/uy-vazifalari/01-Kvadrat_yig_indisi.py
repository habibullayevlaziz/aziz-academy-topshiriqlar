# for siklida sonlar kvadratini yig'indisini toping
# 1, 3 -> 1 + 4 + 9 = 14
n = int(input())
yigindi = 0
for i in range(1, n):
    yigindi += i ** 2
print(yigindi)