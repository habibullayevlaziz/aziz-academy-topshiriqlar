import sys
from collections import Counter
matn = sys.stdin.read()
sozlar = matn.split()
sozlar_soni = Counter(sozlar)
saralangan_sozlar = sorted(sozlar_soni)
for soz in saralangan_sozlar:
    print(f"{soz} {sozlar_soni[soz]}")