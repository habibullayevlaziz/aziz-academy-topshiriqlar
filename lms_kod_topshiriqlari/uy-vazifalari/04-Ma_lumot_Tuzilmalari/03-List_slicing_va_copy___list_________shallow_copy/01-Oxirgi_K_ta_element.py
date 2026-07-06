import sys
data = sys.stdin.read().split()
k = int(data[-1])
lst = data[:-1]
print(*lst[-k:])