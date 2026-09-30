items = input().split()
seen = []
for x in items:
    if x not in seen:
        seen.append(x)
print(" ".join(seen))