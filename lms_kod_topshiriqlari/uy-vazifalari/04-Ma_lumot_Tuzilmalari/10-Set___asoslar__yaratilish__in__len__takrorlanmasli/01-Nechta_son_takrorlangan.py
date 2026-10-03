sonlar = input().split()
seen = set()
dups = set()
for x in sonlar:
    if x in seen:
        dups.add(x)
    else:
        seen.add(x)
print(len(dups))