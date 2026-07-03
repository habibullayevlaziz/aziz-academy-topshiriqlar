s = input().split()
n = len(s)
del s[(n - 1) // 2 : n // 2 + 1]
print(*s)