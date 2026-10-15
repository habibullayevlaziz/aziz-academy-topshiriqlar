n = int(input())
names = []
for i in range(n):
    names.append(input())
w = 0
for name in names:
    if len(name) > w:
        w = len(name)
for name in names:
    print(name.ljust(w) + "|")