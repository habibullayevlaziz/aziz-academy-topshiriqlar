kwh = int(input())
if kwh <= 100:
    pul = kwh * 450
elif kwh <= 200:
    pul = (100 * 450) + (kwh - 100) * 600
else:
    pul = (100 * 450) + (100 * 600) + (kwh - 200) * 900
print(pul)