import sys
lines = sys.stdin.read().splitlines()
line1 = lines[0].split()
line2 = set(lines[1].split())
res = []
for x in line1:
    if x in line2 and x not in res:
        res.append(x)
print(*res)