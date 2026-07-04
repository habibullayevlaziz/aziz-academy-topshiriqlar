N = int(input())
musbat_soni = 0
manfiy_soni = 0
for _ in range(N):
    son = int(input())
    if son > 0:
        musbat_soni += 1
    elif son < 0:
        manfiy_soni += 1
print(f"{musbat_soni} {manfiy_soni}")