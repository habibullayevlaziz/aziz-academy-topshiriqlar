import sys
data = [line.split() for line in sys.stdin.read().splitlines() if line.strip()][1:]
best = min(data, key=lambda x: (-int(x[1]), x[0]))
print(*best)