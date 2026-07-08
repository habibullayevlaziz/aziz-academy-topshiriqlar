import sys
data = sys.stdin.read().splitlines()
n = int(data[0])
d = dict(x.split() for x in data[1:n+1] if x.strip())
print(d.get(data[-1].strip(), "Topilmadi"))