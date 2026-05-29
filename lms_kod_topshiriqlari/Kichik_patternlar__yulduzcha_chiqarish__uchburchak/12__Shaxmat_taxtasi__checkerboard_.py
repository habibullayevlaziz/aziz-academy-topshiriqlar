n, m = map(int, input().split())
for i in range(n):
    satr = ''
    for j in range(m):
        if(i + j) % 2 == 0:
            satr += '*'
        else:
            satr += '.'
    print(satr)