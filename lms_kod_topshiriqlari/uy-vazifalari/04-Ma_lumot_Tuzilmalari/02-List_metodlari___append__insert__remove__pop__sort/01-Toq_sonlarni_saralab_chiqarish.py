import sys 
print(*sorted(x for x in map(int, sys.stdin.read().split()[1:]) if x % 2 != 0))