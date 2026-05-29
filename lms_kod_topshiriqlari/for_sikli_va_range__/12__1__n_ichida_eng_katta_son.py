n = int(input())
max_son = 0
for i in range(1, n + 1):
    if i > max_son:
        max_son = i
print(max_son)