import sys
data = sys.stdin.read().split()
idx = int(data[-1])
lst = data[:-1]
lst.pop(idx)
print(*lst)