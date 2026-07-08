import sys
lines = sys.stdin.read().splitlines()
set1 = set(map(int, lines[0].split()))
set2 = set(map(int, lines[1].split()))
print(*sorted(set1 ^ set2))