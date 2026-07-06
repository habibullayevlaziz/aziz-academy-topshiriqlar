import sys
orig = sys.stdin.read().split()
print(*orig)
print(*sorted(orig, key=int))