import sys
seen = set()
dups = set()
for x in sys.stdin.read().split():
    if x in seen:
        dups.add(x)
    else:
        seen.add(x)
print(len(dups))