soz = input()
sanoq = {}
for harf in soz:
    sanoq[harf] = sanoq.get(harf, 0) + 1
for harf, soni in sanoq.items():
    print(f"{harf} {soni}")