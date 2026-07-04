N = int(input())
musbat_yigindi = 0
musbat_soni = 0
for _ in range(N):
    son = int(input())
    if son > 0:
        musbat_yigindi += son
        musbat_soni += 1
if musbat_soni > 0:
    print(musbat_yigindi // musbat_soni)
else:
    print(0)