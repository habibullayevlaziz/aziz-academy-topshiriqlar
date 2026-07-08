import sys
from collections import Counter
s = sys.stdin.read().strip()
c = Counter(s)
for k in sorted(c):
    print(k, c[k])