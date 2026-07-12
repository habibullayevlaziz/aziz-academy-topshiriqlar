import sys
matn = sys.stdin.read()
words = matn.split()
natija = [w for w in words if len(w) >= 5]
print(natija)