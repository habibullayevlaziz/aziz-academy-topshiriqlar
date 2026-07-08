import sys
lines = [set(map(int, line.split())) for line in sys.stdin.read().splitlines()if line.strip()]
if lines:
    print(*(sorted(set.intersection(*lines))))