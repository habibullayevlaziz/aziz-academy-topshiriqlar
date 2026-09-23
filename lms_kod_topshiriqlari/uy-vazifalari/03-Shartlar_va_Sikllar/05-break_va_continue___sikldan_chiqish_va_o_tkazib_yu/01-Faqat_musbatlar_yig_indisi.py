n = int(input())
yigindi = 0
sikl_soni = 0
while sikl_soni < n:
    son = int(input())
    sikl_soni += 1
    if son <= 0:
        continue
    yigindi += son
print(yigindi)