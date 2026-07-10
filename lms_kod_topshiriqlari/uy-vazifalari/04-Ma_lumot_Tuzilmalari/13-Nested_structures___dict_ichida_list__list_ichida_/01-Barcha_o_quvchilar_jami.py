import sys
data = sys.stdin.read().splitlines()
if data:
    n = int(data[0])
    total = sum(len(line.split()) - 1 for line in data[1 : n + 1] if line.strip())
    print(total)