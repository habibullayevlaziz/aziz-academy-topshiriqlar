import sys
print(sum(int(x) for x in sys.stdin.read().split()[1:] if x.isdigit()))