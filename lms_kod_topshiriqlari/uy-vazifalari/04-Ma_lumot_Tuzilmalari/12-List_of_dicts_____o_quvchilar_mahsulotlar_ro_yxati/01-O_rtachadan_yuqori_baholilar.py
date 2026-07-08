import sys
lines = [line.split() for line in sys.stdin.read().splitlines()[1:] if line.strip()]
avg = sum(int(p[1]) for p in lines) / len(lines)
for name, val in lines:
    if int(val) > avg:
        print(name)