n, m = map(int, input().split())
for i in range(n):
    for j in range(1, m + 1):
        if j == m:
            print(j, end="")
        else:
            print(j, end=" ")
    print()