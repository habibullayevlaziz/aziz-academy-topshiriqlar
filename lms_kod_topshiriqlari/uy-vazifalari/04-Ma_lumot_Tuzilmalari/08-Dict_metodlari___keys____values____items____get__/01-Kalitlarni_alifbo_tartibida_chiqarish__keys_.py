import sys
data = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
names = sorted([x.split()[0] for x in data[1:]])
print(*names)