import sys
for line in sys.stdin.read().splitlines()[1:]:
     if line.strip():
        p = line.split()
        print(p[0], sum(map(int, p[1:])))