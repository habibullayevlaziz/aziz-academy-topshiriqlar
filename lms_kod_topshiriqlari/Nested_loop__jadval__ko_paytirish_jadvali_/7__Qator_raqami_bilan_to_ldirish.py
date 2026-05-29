n, m = map(int,input().split())
for i in range(1, n + 1):
    print((str(i) + " ") * (m - 1) + str(i))