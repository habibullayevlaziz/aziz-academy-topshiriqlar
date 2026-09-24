# Kodingizni shu yerga yozing
from collections import Counter
sanoq = Counter(input().split())
print(sum(1 for x in sanoq.values() if x > 1))