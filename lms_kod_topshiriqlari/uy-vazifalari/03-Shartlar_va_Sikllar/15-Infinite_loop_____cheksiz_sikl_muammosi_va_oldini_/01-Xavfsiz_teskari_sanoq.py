import sys
n = int(sys.stdin.read().strip())
print(*(list(range(n, 0, -1)) + ["BOOM"]), sep="\n")