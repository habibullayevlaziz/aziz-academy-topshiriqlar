import sys
lines = [set(map(int, line.split())) for line in sys.stdin.read().splitlines() if line.strip()]
if lines[0].issubset(lines[1]):
    print("Ha")
else:
    print("Yoq")