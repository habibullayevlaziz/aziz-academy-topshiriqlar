import sys
data = sys.stdin.read().split()
val = data[-1]
lst = data[:-1]
lst.remove(val)
print(*lst)