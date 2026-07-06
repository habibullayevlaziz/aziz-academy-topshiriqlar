import sys
res = sorted(map(int, sys.stdin.read().split()[1:]))
print(*res)