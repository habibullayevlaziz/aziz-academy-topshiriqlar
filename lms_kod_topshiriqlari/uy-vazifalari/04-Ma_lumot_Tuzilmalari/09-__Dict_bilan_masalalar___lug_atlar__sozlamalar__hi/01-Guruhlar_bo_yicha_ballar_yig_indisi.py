import sys
from collections import Counter
c = Counter()
for k, v in [x.split() for x in sys.stdin.read().splitlines() if x.strip()][1:]:
    c[k] += int(v)
for k in sorted(c):
    print(k, c[k])